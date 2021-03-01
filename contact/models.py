from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Messages(models.Model):
    name = models.CharField(max_length=50, blank=False,
                            null=False, verbose_name='Nome')
    email = models.EmailField(verbose_name='e-Mail')
    subject = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Assunto')
    message = RichTextField(
        blank=False, null=False, max_length=1000, verbose_name="Mensagem")
    created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('message', args=[self.pk])

    def get_absolute_url_delete(self):
        return reverse('delete_message', args=[self.pk])
