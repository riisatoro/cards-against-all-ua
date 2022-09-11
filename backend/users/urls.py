from django.urls import path

from users.views import CreateUserView, UserDataView


urlpatterns = [
    path('', UserDataView.as_view()),
    path('register/', CreateUserView.as_view()),
]
