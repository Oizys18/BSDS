from django.urls import path
import images.views as views


urlpatterns = [
    path('', views.Image_Classifier.as_view(), name='predict'),
]
