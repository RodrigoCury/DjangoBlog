from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import BlogPost

# Create your views here.


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog/post_new.html"
    fields = ['title', 'content', 'author']


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content', 'author']


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('home')
