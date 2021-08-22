# Create your views here.
from django.shortcuts import render
from .models import Post


# from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        "posts": posts
    }
    return render(request, 'tour_app/index.html', context)


def about(request):
    return render(request, 'tour_app/about.html')
