from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Link an User to a BlogPost
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\



class BlogPost(models.Model):
    STATUS = (
        ('rascunho', "Rascunho"),
        ('publicado', "Publicado")
    )  # tuple of dual tuples
    title = models.CharField(blank=False, max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # Obrigatório
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="rascunho")
    publishedmanager = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse("post_delete", args=[self.slug])

    class Meta:
        # "-MODEL_COLUMN" => ordem decrescente/ "MODEL_COLUMN" => ordem crescente
        ordering = ("-published",)

    def __str__(self):
        return f"{self.title}"


@receiver(pre_save, sender=BlogPost)
def insert_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
