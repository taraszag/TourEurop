# Create your views here.
from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filter import PostFilter


# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        "posts": posts
    }
    return render(request, 'tour_app/index.html', context)


def page_not_found(request, exception):
    context = None
    if "tried" in str(exception):
        context = {"exception": "Page not found"}
    else:
        context = {"exception": exception}
    return render(request, "tour_app/404.html", context)


class FilterPostListView(ListView):
    filter_class = None

    def get_queryset(self):
        qs = super().get_queryset()
        req = self.request.GET
        self.filtered = self.filter_class(req, qs)
        return self.filtered.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filtered
        return context


class PostListView(FilterPostListView):
    model = Post
    filter_class = PostFilter
    template_name = "tour_app/index.html"
    context_object_name = "posts"
    paginate_by = 5


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
