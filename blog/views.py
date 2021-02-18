from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = 'blogpost'
