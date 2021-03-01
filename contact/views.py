from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Messages
from .forms import MessagesForm
# Create your views here.


class MessagesListView(UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Messages
    template_name = 'messages_list.html'
    paginate_by = 10


class MessagesCreateView(CreateView):
    model = Messages
    form_class = MessagesForm
    template_name = 'new_message.html'

    # def success_message(self):
    #     return f'Mensagem enviada com sucesso!! Tentarei responder rápido.'


class MessagesDetailView(UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Messages
    template_name = "message.html"
    context_object_name = 'mensagem'


class MessagesDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Messages
    template_name = 'message_delete.html'
    success_url = reverse_lazy('message_list')
