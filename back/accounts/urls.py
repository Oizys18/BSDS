from django.urls import path
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        #
        title="LostAndFound API",
        default_version="v1",
        #
        description='아자아자',
        contact=openapi.Contact(email='jay.hyundong@gmail.com'),
        license=openapi.License(name='SSAFY License'),
    )
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
    path('<int:user_id>/', views.user_detail, name='user_detail'),
]
