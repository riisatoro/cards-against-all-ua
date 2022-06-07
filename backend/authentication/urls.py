from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('access/', TokenObtainPairView.as_view(), name='get_auth_tokens'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_auth_tokens'),
]
