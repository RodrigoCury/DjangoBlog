from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.MessagesListView.as_view(), name="message_list"),
    path('', views.MessagesCreateView.as_view(), name='new_message'),
    path('<int:pk>/', views.MessagesDetailView.as_view(), name='message'),
    path('<int:pk>/delete', views.MessagesDeleteView.as_view(), name='delete_message')
]
