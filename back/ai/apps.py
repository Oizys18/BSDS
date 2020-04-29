from django.apps import AppConfig
import os
import tensorflow as tf
from tensorflow.python.keras.metrics import top_k_categorical_accuracy
import json


def top_3_accuracy(true, pred):
    return top_k_categorical_accuracy(true, pred, 3)


class AiConfig(AppConfig):
    name = 'ai'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_FOLDER = os.path.join(BASE_DIR, 'ai', 'model')
    MODEL_FILE = os.path.join(MODEL_FOLDER, "sequential_ft.h5")
    model = tf.keras.models.load_model(MODEL_FILE, custom_objects={
                                       'top_3_accuracy': top_3_accuracy})
    COLOR_MODEL_FILE = os.path.join(MODEL_FOLDER, "model.json")
    COLOR_MODEL_WEIGHT_FILE =  os.path.join(MODEL_FOLDER, "model_weights.h5")
    color_model = tf.keras.models.model_from_json(
        json.load(open(COLOR_MODEL_FILE))["model"], custom_objects={})
    color_model.load_weights(COLOR_MODEL_WEIGHT_FILE)
