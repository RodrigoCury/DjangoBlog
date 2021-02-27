from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name="home"),
    path('post/new/', views.BlogCreateView.as_view(), name="post_new"),
    path('post/categories/', views.CategoryListView.as_view(), name="categories"),
    path('post/categories/<slug:slug>/',
         views.CategoryDetailView.as_view(), name='category_posts'),
    path('post/<slug:slug>/', views.BlogDetailView.as_view(), name="post_detail"),
    path('post/<slug:slug>/edit', views.BlogUpdateView.as_view(), name="post_edit"),
    path('post/<slug:slug>/delete',
         views.BlogDeleteView.as_view(), name="post_delete"),
    path("hello", views.hello, name="hello")

]
