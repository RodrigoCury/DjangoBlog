from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import BlogPost

# Create your views here.


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = 'blogpost'


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog/post_new.html"
    fields = '__all__'
