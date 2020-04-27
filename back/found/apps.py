from django.apps import AppConfig
import os


class FoundConfig(AppConfig):
    name = 'found'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_FOLDER = os.path.join(BASE_DIR, 'ai', 'model')

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))