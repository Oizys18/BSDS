from django.apps import AppConfig
import os
import tensorflow as tf
from tensorflow.python.keras.metrics import top_k_categorical_accuracy


def top_3_accuracy(true, pred):
    return top_k_categorical_accuracy(true, pred, 3)


class FoundConfig(AppConfig):
    name = 'found'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_FOLDER = os.path.join(BASE_DIR, 'ai', 'model')
    MODEL_FILE = os.path.join(MODEL_FOLDER, "sequential_ft.h5")
    model = tf.keras.models.load_model(MODEL_FILE, custom_objects={
                                       'top_3_accuracy': top_3_accuracy})  # custom?
    # https://github.com/JeonCS/keras-flask-deployment/blob/master/util.py
