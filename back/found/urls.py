from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_found, name='search_found'),
    path('search/image/', views.search_by_image, name='search_by_image'),

    path('posting/image/', views.create_found_image, name='create_found_image'),
    path('posting/', views.create_found, name='create_found'),
    path('posting/admin/list/', views.get_user_found_list, name='get_user_found_list'),
    path('posting/list/<int:found_id>/', views.get_found_detail, name='get_found_detail'),
    path('posting/<int:found_id>/', views.update_delete_found, name='update_delete_found'),
    path('posting/<int:found_id>/status/', views.update_found_status, name='update_found_status'),
]
