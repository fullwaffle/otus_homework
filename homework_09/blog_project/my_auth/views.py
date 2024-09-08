from django.contrib.auth.views import UserModel
from django.views.generic import CreateView

from .forms import BlogUserCreateForm


class BlogUserCreateView(CreateView):
    model = UserModel
    success_url = "/"
    form_class = BlogUserCreateForm
