from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

from .forms import FoundPostingForm, FoundImageForm
from .models import FoundPosting, FoundImage
import json
from django.http import JsonResponse, HttpResponseBadRequest


@require_GET
def posting_list(request):
    postings = FoundPosting.objects.all()
    dataset = json.dumps(postings, ensure_ascii=False)
    return HttpResponse(dataset)


# @login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    images = request.FILES.getlist('file')
    if request.method == 'POST':
        posting_form = FoundPostingForm(request.POST)
        if posting_form.is_valid() and len(images) <= 5:
            posting = posting_form.save(commit=False)
            posting.user = request.user
            posting.save()

            for image in images:
                request.FILES['file'] = image
                image_form = FoundImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting
                    image.save()
            return HttpResponse('200')
    else:
        posting_form = FoundPostingForm()
        image_form = FoundImageForm()
    return HttpResponse('400')
