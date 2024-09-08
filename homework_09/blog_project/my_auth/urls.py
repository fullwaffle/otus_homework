from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import BlogUserCreateView

app_name = "my_auth"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", BlogUserCreateView.as_view(), name="register"),
]
