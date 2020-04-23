from django.urls import path
from . import views

app_name = 'found'

urlpatterns = [
    path('', views.posting_list, name='posting_list'),
    path('create/', views.create_posting, name='create_posting'),
]
