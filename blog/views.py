from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
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
    fields = ['title', 'content', 'author', 'status']

    def success_message(title):
        return f"{title} foi criado com sucesso"


class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    success_message = "%(calculated_field)s alterado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = BlogPost
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)
