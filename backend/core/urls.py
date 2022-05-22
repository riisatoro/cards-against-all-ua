from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from authentication.urls import urlpatterns as authentication_urls


documentation_urls = [ 
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


api_urls = [
    path('token/', include(authentication_urls)),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include(documentation_urls)),
    path('api/', include(api_urls)),
]
