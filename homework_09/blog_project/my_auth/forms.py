from django.contrib.auth.views import UserModel
from django.contrib.auth.forms import UserCreationForm


class BlogUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2")
