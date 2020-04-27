from django.apps import AppConfig
import os
import tensorflow as tf


class FoundConfig(AppConfig):
    name = 'found'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_FOLDER = os.path.join(BASE_DIR, 'ai', 'model')
    MODEL_FILE = os.path.join(MODEL_FOLDER, "model.h5")
    model = tf.keras.models.load_model(MODEL_FILE)
