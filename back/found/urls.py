from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


urlpatterns = [
    path('', views.posting_list, name='posting_list'),  # R - no img
    # path('', views.posting_img_search, name='img_search'),  # 이미지 제출

    # path('create/', views.create_posting, name='create_posting'),
]

"""
할 일
1. migrate -> color, category 수정
2. url 짜야 하는 것들 먼저 기획
3. database 손보고 넣기
"""
