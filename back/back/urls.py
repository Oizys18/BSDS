from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        #
        title="분실둥실 API",
        default_version="v1",
        #
        description='아자아자',
        contact=openapi.Contact(email='jay.hyundong@gmail.com'),
        license=openapi.License(name='SSAFY License'),
    )
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('images/', include('images.urls')),

    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),

    path('api-token/', obtain_jwt_token),

    path('user/', include('accounts.urls')),
    path('found/', include('found.urls')),
    path('lost/', include('lost.urls')),
]
