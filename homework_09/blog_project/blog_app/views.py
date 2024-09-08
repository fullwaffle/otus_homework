from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()

        return context
