# search_by_image 관련 module
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
from PIL import Image


# create_found_image 관련 함수
def prepare_image(img):
    # convert to handle png file format
    img = Image.open(io.BytesIO(img)).convert(mode='RGB')
    img = img.resize((224,224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def parse_result(pred, cat_code):
    pred_classes = np.argsort(pred[0])[-3:][::-1]
    pred_probs = np.sort(pred[0])[-3:][::-1]
    result = [(cat_code[str(pred_classes[i])],pred_probs[i]) for i in range(3)]
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
    print(first, second, third)

    # return
    images_id_result = [int(first), int(second), int(third)]

    return images_id_result
