from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('about/', TemplateView.as_view(template_name="blog/about.html"), name="about"),
    path('post/new/', views.BlogCreateView.as_view(), name="post_new"),
    path('post/categories/', views.CategoryListView.as_view(), name="categories"),
    path('post/categories/<slug:slug>/',
         views.CategoryDetailView.as_view(), name='category_posts'),
    path('post/<slug:slug>/', views.BlogDetailView.as_view(), name="post_detail"),
    path('post/<slug:slug>/edit', views.BlogUpdateView.as_view(), name="post_edit"),
    path('post/<slug:slug>/delete',
         views.BlogDeleteView.as_view(), name="post_delete"),
]
