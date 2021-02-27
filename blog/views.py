from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import BlogPost, Category
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


@login_required
def hello(request):
    return HttpResponse("Logado")


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/categories_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/categories.html'


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"


class BlogCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser

    form_class = BlogPostForm
    model = BlogPost
    template_name = "blog/post_new.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

    def success_message(title):
        return f"{title} foi criado com sucesso"


class BlogUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser

    form_class = BlogPostForm
    model = BlogPost
    template_name = 'blog/post_edit.html'
    success_message = "%(calculated_field)s alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        print(obj.category)
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class BlogDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = BlogPost
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)
