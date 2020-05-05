from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import LostPosting, LostThumbnail
from .serializers import LostImageSerializer, LostThumbnailSerializer, LostPostingSerializer, \
    LostPostingDetailSerializer, AdminLostDetailSerializer, AdminLostListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
import hashlib
from django.core.cache import cache
from django.core.mail import send_mail
from back.settings import EMAIL_HOST_USER
from ai.views import get_numpy_path, get_category, get_closer_user, get_hex, hex_to_rgb, get_color
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def create_lost_image(request):
    if request.FILES:
        serializer = LostImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = LostThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                image = serializer.create(serializer.validated_data)
                thumbnail_image = th_serializer.create(th_serializer.validated_data)
                thumbnail_image.origin_id = image.id
                thumbnail_image.save()

                numpy_path = get_numpy_path(image)
                image.numpy_path = numpy_path

                colorData = request.data['colorData']
                hexData = get_hex(colorData)
                r, g, b = hex_to_rgb(hexData)
                colorValue = get_color(r, g, b)

                c1, c2, c3 = get_category(request.FILES['image'])
                image.category_1, image.category_2, image.category_3 = c1, c2, c3
                image.save()

                datasets = {
                    'image_id': thumbnail_image.id,
                    'category': c1,
                    'color': colorValue,
                }

                return Response(status=200, data=datasets, content_type='application.json')
        return Response(status=400, data={'message': 'Invalid images input'})
    return Response(status=403, data={'message': '이미지는 필수 값입니다.'})


@api_view(['POST'])
@permission_classes([AllowAny])
def create_lost(request):
    data = request.data
    serializer = LostPostingSerializer(data=data)
    if serializer.is_valid():

        password = hashlib.sha256(data['password'].encode()).hexdigest()
        lostname = password[-5:] + datetime.today().strftime('%d%H%f')
        posting = serializer.save(password=password, lostname=lostname, status=False)

        if data.get('x'):
            flag, users = get_closer_user(data['x'], data['y'], 1000)
            if not flag and users:
                if len(users) > 1:
                    posting.p1, posting.p2 = users[0], users[1]
                else:
                    posting.p1 = users[0]

        posting.save()

        if data.get('image_id'):
            thumbnail = get_object_or_404(LostThumbnail, id=data['image_id'])
            thumbnail.posting_id = posting.id
            thumbnail.save()

        datasets = {
            'lost_id': posting.id,
            'lostname': posting.lostname,
        }

        return Response(status=200, data=datasets)
    return Response(status=400, data={'message': 'Invalid input'})


@api_view(['POST'])
@permission_classes([AllowAny])
def lost_login(request):
    posting = get_object_or_404(LostPosting, lostname=request.data['lostname'])
    password = hashlib.sha256(request.data['password'].encode()).hexdigest()
    if posting.password == password:
        serializer = LostPostingDetailSerializer(posting)
        return Response(status=200, data=serializer.data)
    return Response(status=400, data={'message': '비밀번호가 일치하지 않습니다.'})


@api_view(['PATCH', 'DELETE'])
@permission_classes([AllowAny])
def update_delete_lost(request, lostname):
    posting = get_object_or_404(LostPosting, lostname=lostname)

    if request.method == 'PATCH':
        serializer = LostPostingSerializer(instance=posting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data=serializer.data)
        return Response(status=400, data={'message': 'Invalid input'})
    elif request.method == 'DELETE':
        posting.delete()
        return Response(status=204)


@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_lost_status(request, lostname):
    posting = get_object_or_404(LostPosting, lostname=lostname)
    posting.status = False if posting.status else True
    posting.save()
    return Response(status=204)


@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_lost_image(request, lostname):
    if request.FILES:
        serializer = LostImageSerializer(request.POST, request.FILES)
        if serializer.is_valid():
            th_serializer = LostThumbnailSerializer(request.POST, request.FILES)
            if th_serializer.is_valid():
                image = serializer.create(serializer.validated_data)
                thumbnail_image = th_serializer.create(th_serializer.validated_data)
                thumbnail_image.origin_id = image.id

                origin_post_id = LostPosting.objects.get(lostname=lostname).id

                origin_thumbnail = get_object_or_404(LostThumbnail, posting_id=origin_post_id)
                origin_thumbnail.posting_id = None
                origin_thumbnail.save()

                thumbnail_image.posting_id = origin_post_id
                thumbnail_image.save()

                colorData = request.data['colorData']
                hexData = get_hex(colorData)
                r, g, b = hex_to_rgb(hexData)
                colorValue = get_color(r, g, b)

                numpy_path = get_numpy_path(image)
                image.numpy_path = numpy_path

                c1, c2, c3 = get_category(request.FILES['image'])
                image.category_1, image.category_2, image.category_3 = c1, c2, c3
                image.save()

                datasets = {
                    'image_id': thumbnail_image.id,
                    'category': c1,
                    'color': colorValue,
                }
                return Response(status=200, data=datasets, content_type='application.json')
        return Response(status=400, data={'message': 'Invalid images input'})
    return Response(status=403, data={'message': '이미지는 필수 값입니다.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lost_list_admin(request):
    user_id = request.user.id
    posting = cache.get(f'admin_lost_{user_id}')
    if not posting:
        posting = LostPosting.objects.filter(Q(p1=user_id) | Q(p2=user_id), status=0)
        cache.set(f'admin_lost_{user_id}', posting, 60*5)

    serializer = AdminLostListSerializer(posting, many=True)

    datasets = {
        'meta': {
            'total': posting.count(),
        },
        'documents': serializer.data
    }

    return Response(status=200, data=datasets)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lost_detail_admin(request, lost_id):
    posting = get_object_or_404(LostPosting, id=lost_id)
    serializer = AdminLostDetailSerializer(posting)

    return Response(status=200, data=serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_lost_notice(request, lost_id):
    posting = get_object_or_404(LostPosting, id=lost_id)
    if posting.email:
        subject = f'[분실둥실] {request.user.center_name}{request.user.role}에서 유사한 분실물을 보관중입니다.'
        message = f'잃어버린 생각이 뭉게뭉게☁ 날 때, 분실물 클라우드 ☁분실둥실☁ 입니다.' \
                  f'{request.user.center_name}{request.user.role}에서 등록하신 분실품({posting.lostname})과 ' \
                  f'유사한 물품을 보관중입니다.' \
                  f'해당 물품을 관할기관에서 수령할 시 본인임을 증명할 수 있는 서류(신분증 등)가 필요할 수 있습니다.' \
                  f'감사합니다.'

        recipient_list = [posting.email]
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list, html_message=message)

    return Response(status=203)

