from django.apps import AppConfig
# import pandas as pd
# from joblib import load
import pickle
import os
import tensorflow as tf

class ImagesConfig(AppConfig):
    name = 'images'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'images\models')
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "model.h5")
    classifier = tf.keras.models.load_model(CLASSIFIER_FILE)