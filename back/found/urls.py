from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


urlpatterns = [
    # 이미지 없는 전체 목록 검색 및 페이지네이션
    path('search/', views.search_found, name='search_found'),
    # 이미지 제출하고 검색 및 페이지네이션
    path('search/image/', views.search_by_image, name='search_by_image'),

    # 글 작성을 위한 이미지 제출
    path('posting/image/', views.create_found_image, name='create_found_image'),
    # 글 작성
    path('posting/', views.create_found, name='create_found'),
    # 자기 게시글 목록 조회
    path('posting/list/', views.get_user_found_list, name='get_user_found_list'),
    # 게시글 디테일 조회
    path('posting/list/<int:found_id>/', views.get_found_detail, name='get_found_detail'),
    # 게시글 수정 및 삭제
    path('posting/<int:found_id>/', views.update_delete_found, name='update_delete_found'),
    # 상태 토글 수정
    path('posting/<int:found_id>/status/', views.update_found_status, name='update_found_status'),

]

"""
할 일

2. url 짜야 하는 것들 먼저 기획
1. 습득물 검색 
    - 이미지 받기
    - 검색하기
    - 결과 리턴하기 (페이지 넘버링)
2. 습득물 검색 결과에 대해 
    - 카테고리 설정
    - 페이지 넘버링
3. 습득물 신고하기
    - 이미지 받기
    - 저장하기
4. 자신이 작성한 습득물 게시글 조회
    - 목록 조회
    - 상세 조회
5. 자신이 작성한 습득물 게시글 수정
    - 내용 수정
    - 상태 수정
6. 자신이 작성한 습득물 게시글 삭제 


3. database 손보고 넣기
"""
