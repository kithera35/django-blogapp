from django.views.generic import(ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from multiprocessing import context
from pdb import post_mortem
from pyexpat import model
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from.models import Post


# def home(req):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(req, 'blog/home.html', context)


# Class-Based View


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by=2


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Getting current logged in user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Getting current logged in user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


def about(req):
    return render(req, 'blog/about.html')
