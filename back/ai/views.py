# search_by_image 관련 module
from django.shortcuts import get_object_or_404
from decouple import config
import requests
import mahotas as mh
import numpy as np
from scipy.spatial import distance
from sklearn.model_selection import cross_validate, LeaveOneOut, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from django.conf import settings
import os
from .apps import AiConfig
import json
import io
import tensorflow as tf
from PIL import Image
from django.contrib.auth import get_user_model
User = get_user_model()


# create_found_image 관련 함수
def prepare_image(img):
    # convert to handle png file format
    img = Image.open(io.BytesIO(img)).convert(mode='RGB')
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def parse_result(pred, cat_code):
    pred_classes = np.argsort(pred[0])[-3:][::-1]
    pred_probs = np.sort(pred[0])[-3:][::-1]
    result = [(cat_code[str(pred_classes[i])], pred_probs[i])
              for i in range(3)]
    return result


def get_numpy_path(image):
    # FoundImage의 numpy_path 칼럼 값 저장
    im = mh.imread(image.image)
    im = mh.colors.rgb2gray(im, dtype=np.uint8)
    im_ftr = mh.features.haralick(im).ravel()
    numpy_path = str(image.image).split('.')[0] + '.npy'

    # image 와 같은 경로 내에 [FoundImage와 같은 이름].npy 파일도 저장
    # numpy_path = os.path.join(settings.MEDIA_ROOT, numpy_path)
    np.save(os.path.join(settings.MEDIA_ROOT, numpy_path), im_ftr)

    return numpy_path


# Create your views here.
def get_category(image):
    # TODO load keras model
    print("---- load Keras model")
    loaded_model = AiConfig.model
    print(loaded_model)  # <tensorflow.python.keras.engine.sequential.Sequential object at 0x00000240F8F3B648>

    # TODO predict (image input & output --> category_1, 2, 3)
    # image = request.FILES["image"]
    print(image)  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
    print(type(image))  # <class 'bytes'>

    image = Image.open(image).convert(mode='RGB')
    print(image)
    image = image.resize((224, 224))
    print(image)
    img_array = np.array(image) / 255.0
    print(img_array)
    print(img_array.shape)
    img_array = np.expand_dims(img_array, axis=0)
    print(img_array)
    print(img_array.shape)

    preds = loaded_model.predict(img_array)
    print(preds)

    path = os.path.join(settings.BASE_DIR, 'found', 'fixtures', 'category_code.json')
    with open(path) as file:
        cat_code = json.loads(file.read())
    print(cat_code)

    print(preds[0])  # <class 'numpy.ndarray'>
    predictions = np.argsort(preds[0]).tolist()
    predictions.reverse()
    predictions = predictions[:3]

    # Category 분석기 결과값
    return predictions[0]+1, predictions[1]+1, predictions[2]+1


def get_similar_image(lost_image, origin_images):
    # 분실자가 Post 한 이미지 전처리 <class 'numpy.ndarray'>
    im = mh.imread(lost_image)
    im = mh.colors.rgb2gray(im, dtype=np.uint8)
    im_ftr = mh.features.haralick(im).ravel()

    # npy file 불러오기
    origin_ids = []
    origin_image_features = []
    for origin_image in origin_images:
        real_numpy_path = os.path.join(settings.MEDIA_ROOT, origin_image.numpy_path)
        print(real_numpy_path)
        origin_image_feature = np.load(real_numpy_path)
        origin_ids.append(origin_image.id)
        print(origin_image_feature)
        origin_image_features.append(origin_image_feature)

    origin_ids = [0] + origin_ids
    origin_image_features = [im_ftr] + origin_image_features

    origin_image_features = np.array(origin_image_features)
    # print(origin_image_features.shape)

    # features & labels numpy.array
    clf = Pipeline([('preproc', StandardScaler()),
                    ('classifier', LogisticRegression())])

    cv = LeaveOneOut()

    # scores = cross_val_score(clf, features, labels, cv=cv)
    # print('Accuracy: {:.2%}'.format(scores.mean()))

    sc = StandardScaler()
    features = sc.fit_transform(origin_image_features)

    # dists matrix 구하기 (사진 개수 X 사진 개수)
    dists = distance.squareform(distance.pdist(features, "cosine"))
    # print(*dists, sep='\n')
    # print(dists[0])
    # print(dists[0].argsort().tolist())
    similar_order = dists[0].argsort().tolist()
    similar_order.reverse()
    print(similar_order)
    first, second, third = similar_order[0], similar_order[1], similar_order[2]
    # TODO 데이터 없어서 지금 오류 나더이다.. 5, 5, 5로 하면 일단 테스트 됩니다.
    print(first, second, third)

    # return
    images_id_result = [int(first), int(second), int(third)]

    return images_id_result


def get_closer_user(x, y, radius):
    keywords = f'x={x}&y={y}&radius={radius}&categoru_group_code=PO3&query=경찰서'
    URL = 'https://dapi.kakao.com/v2/local/search/keyword.json?&sort=distance&'
    headers = {"Authorization": f"KakaoAK {config('KAKAOAK')}"}

    url = URL + keywords
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)

    flag = False
    users = []

    if result.get('meta'):
        for item in result['documents']:
            if User.objects.filter(phone_number=item['phone']).exists():
                users.append(get_object_or_404(User, phone_number=item['phone']).id)
    else:
        flag = True

    return flag, users


def get_hex(colorData):
    print(colorData)
    colorData = colorData.split(',')
    hex_list, pop_list = colorData[:len(colorData)//2], colorData[len(colorData)//2:]
    pop_list = [int(i) for i in pop_list]
    color_hex = hex_list[pop_list.index(max(pop_list))]
    # TODO hex 라는 변수는 사용하면 안댑니당!! 내장함수가 있기때문에 주의하셔용~
    return color_hex


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def get_color(r, g, b):
    labelsValues = [
        "red-ish",
        "green-ish",
        "blue-ish",
        "orange-ish",
        "yellow-ish",
        "pink-ish",
        "purple-ish",
        "brown-ish",
        "grey-ish"
    ]

    labelsDict = {
        "red-ish": 1,
        "green-ish": 5,
        "blue-ish": 4,
        "orange-ish": 2,
        "yellow-ish": 3,
        "pink-ish": 6,
        "purple-ish": 7,
        "brown-ish": 8,
        "grey-ish": 9,
    }

    # LOADING MODEL
    model = AiConfig.color_model
    path = AiConfig.COLOR_MODEL_WEIGHT_FILE
    model.load_weights(path)
    print(model)
    print(path)

    r = r / 255
    g = g / 255
    b = b / 255
    # 254 0 2 orange-ish
    # 12 255 2 red-ish
    t = np.argmax(model.predict(tf.constant([[r, g, b]], dtype=tf.float32)))
    print(labelsValues[t])
    return labelsDict[labelsValues[t]]
