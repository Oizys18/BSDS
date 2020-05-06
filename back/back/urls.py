from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api-token/', obtain_jwt_token),

    path('user/', include('accounts.urls')),
    path('found/', include('found.urls')),
    path('lost/', include('lost.urls')),
]

urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
        )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
