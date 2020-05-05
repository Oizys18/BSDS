from django.shortcuts import get_object_or_404
from decouple import config
import requests
import mahotas as mh
import numpy as np
from scipy.spatial import distance
from sklearn.model_selection import LeaveOneOut
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


def prepare_image(img):
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
    im = mh.imread(image.image)
    im = mh.colors.rgb2gray(im, dtype=np.uint8)
    im_ftr = mh.features.haralick(im).ravel()
    numpy_path = str(image.image).split('.')[0] + '.npy'

    np.save(os.path.join(settings.MEDIA_ROOT, numpy_path), im_ftr)

    return numpy_path


def get_category(image):
    loaded_model = AiConfig.model

    image = Image.open(image).convert(mode='RGB')
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    preds = loaded_model.predict(img_array)

    path = os.path.join(settings.BASE_DIR, 'found', 'fixtures', 'category_code.json')
    with open(path) as file:
        cat_code = json.loads(file.read())

    predictions = np.argsort(preds[0]).tolist()
    predictions.reverse()
    predictions = predictions[:3]

    return predictions[0]+1, predictions[1]+1, predictions[2]+1


def get_similar_image(lost_image, origin_images):
    im = mh.imread(lost_image)
    im = mh.colors.rgb2gray(im, dtype=np.uint8)
    im_ftr = mh.features.haralick(im).ravel()

    origin_ids = []
    origin_image_features = []
    for origin_image in origin_images:
        real_numpy_path = os.path.join(settings.MEDIA_ROOT, origin_image.numpy_path)
        origin_image_feature = np.load(real_numpy_path)
        origin_ids.append(origin_image.id)
        origin_image_features.append(origin_image_feature)

    origin_ids = [0] + origin_ids
    origin_image_features = [im_ftr] + origin_image_features

    origin_image_features = np.array(origin_image_features)

    clf = Pipeline([('preproc', StandardScaler()),
                    ('classifier', LogisticRegression())])

    cv = LeaveOneOut()

    sc = StandardScaler()
    features = sc.fit_transform(origin_image_features)

    dists = distance.squareform(distance.pdist(features, "cosine"))

    similar_order = dists[0].argsort().tolist()

    first, second, third = origin_ids[similar_order[1]], origin_ids[similar_order[2]], origin_ids[similar_order[3]]
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
    colorData = colorData.split(',')
    hex_list, pop_list = colorData[:len(colorData)//2], colorData[len(colorData)//2:]
    pop_list = [int(i) for i in pop_list]
    color_hex = hex_list[pop_list.index(max(pop_list))]
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

    model = AiConfig.color_model
    path = AiConfig.COLOR_MODEL_WEIGHT_FILE
    model.load_weights(path)

    r = r / 255
    g = g / 255
    b = b / 255

    t = np.argmax(model.predict(tf.constant([[r, g, b]], dtype=tf.float32)))
    return labelsDict[labelsValues[t]]
