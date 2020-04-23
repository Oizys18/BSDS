from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('images/', include('images.urls')),

    # path('api-token/', obtain_jwt_token),
    path('auth/', include('accounts.urls')),

    path('found/', include('found.urls')),
    path('lost/', include('lost.urls')),
]
