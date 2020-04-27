from django.urls import path
from . import views

app_name = 'lost'

urlpatterns = [
    path('posting/image/', views.create_lost_image, name='create_lost_image'),
    path('posting/', views.create_lost, name='create_lost'),
    path('', views.lost_login, name='lost_login'),
    path('posting/<str:lostname>/', views.update_delete_lost, name='update_delete_lost'),
    path('posting/<str:lostname>/image/', views.update_lost_image, name='update_lost_image'),
    path('posting/<str:lostname>/status/', views.update_lost_status, name='update_lost_status'),

    path('admin/', views.get_lost_list_admin, name='get_lost_list_admin'),
    path('admin/<int:lost_id>/', views.get_lost_detail_admin, name='get_lost_detail_admin'),
    path('admin/<int:lost_id>/notice/', views.send_lost_notice, name='send_lost_notice'),
]
