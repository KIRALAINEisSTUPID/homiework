from venv import create

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from app.models import Post


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class BlogView(ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'posts'


class UpdatePostView(UpdateView):
    model = Post
    fields = ['img', 'title']
    template_name = 'update.html'
    success_url = reverse_lazy('blog')

class DeletePostView(DeleteView):
    model = Post
    fields = ['img', 'title']
    template_name = 'delete.html'
    success_url = reverse_lazy('blog')


class CreatePostView(CreateView):
    model = Post
    fields = ['img', 'title']
    template_name = 'create.html'
    success_url = reverse_lazy('blog')



class DetalPostView(DetailView):
    template_name = 'detail.html'
    model = Post
