from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .forms import BlogPostForm
from .models import BlogPost, Category
# Create your views here.


class CategoryListView(ListView):
    model = Category
    paginate_by = 6
    template_name = 'blog/categories_list.html'

# {'paginator': < django.core.paginator.Paginator object at 0x7ff7f003a1f0 > ,
#  'page_obj': < Page 1 of 2 >,
#  'is_paginated': True,
#  'object_list': < QuerySet [ < Category: Machine Learning > , < Category: Pessoal > ] > ,
#  'category_list': < QuerySet [ < Category: Machine Learning > , < Category: Pessoal > ] > ,
#  'view': < blog.views.CategoryListView object at 0x7ff7f0017670 >}


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        posts_list = self.object.get_posts.all()
        paginator = Paginator(posts_list, 6)
        page = self.request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        context['page_obj'] = paginator.get_page(page)
        return context


class BlogListView(ListView):
    model = BlogPost
    paginate_by = 5
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
