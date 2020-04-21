from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .apps import ImagesConfig
# import pandas as pd

from rest_framework.permissions import IsAuthenticated
from .throttles import LimitedRateThrottle, BurstRateThrottle


# Class based view to predict based on IRIS model
class Image_Classifier(APIView):
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [LimitedRateThrottle]

    def post(self, request, format=None):
        data = request.data
        print(data)
        # keys = []
        # values = []
        # for key in data:
            # keys.append(key)
            # values.append(data[key])
        # X = pd.Series(values).to_numpy().reshape(1, -1)

        loaded_classifier = ImagesConfig.classifier
        print('확인')
        print(loaded_classifier)
        # y_pred = loaded_classifier.predict(X)
        # y_pred = pd.Series(y_pred)
        # target_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        # y_pred = y_pred.map(target_map).to_numpy()
        response_dict = {"Practice": "Practicing"}
        return Response(response_dict, status=200)
