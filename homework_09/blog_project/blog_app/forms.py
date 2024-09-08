from django.forms import ModelForm

from .models import Post, Comment


class PostCreateUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class CommentCreateUpdateForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
