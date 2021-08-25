# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


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
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = "tour_app/user_posts.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(Author=user)


class PostDetailViews(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["NameTour", "TypeTour", "Price", "Photo"]

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["NameTour", "TypeTour", "Price", "Photo"]

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.Author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.Author


def about(request):
    return render(request, 'tour_app/about.html')


def help_fq(request):
    return render(request, 'tour_app/help.html')
