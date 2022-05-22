from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


documentation_urls = [ 
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


api_urls = [
    path('token/', include('authentication.urls')),
    path('user/', include('users.urls')),
    path('game/', include('gamecore.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include(documentation_urls)),
    path('api/', include(api_urls)),
]
