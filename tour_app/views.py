# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        "posts": posts
    }
    return render(request, 'tour_app/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = "tour_app/index.html"
    context_object_name = "posts"


class PostDetailViews(DetailView):
    model = Post

def about(request):
    return render(request, 'tour_app/about.html')


def help_fq(request):
    return render(request, 'tour_app/help.html')
