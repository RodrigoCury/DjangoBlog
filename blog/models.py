from ckeditor.fields import RichTextField
from django.contrib.auth.models import User  # Link an User to a BlogPost
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Nome')
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name="Imagem",
                              upload_to='blog',
                              null=True,
                              blank=True)
    description = models.TextField(max_length=50,
                                   blank=False,
                                   null=False)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ('created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_posts', args=[self.slug])

    @property
    def view_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="400">')

    @property
    def sort(self):
        return Category.objects.all().order_by('name')


class BlogPost(models.Model):
    STATUS = (
        ('rascunho', "Rascunho"),
        ('publicado', "Publicado")
    )  # tuple of dual tuples
    title = models.CharField(verbose_name='Título',
                             blank=False,
                             max_length=50)
    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # Obrigatório
    category = models.ManyToManyField(Category,
                                      related_name='get_posts',)
    image = models.ImageField(verbose_name="Imagem",
                              upload_to='blog',
                              blank=True,
                              null=True)
    content = RichTextField(verbose_name='Conteudo',
                            config_name='content_editor')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="rascunho")

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse("post_delete", args=[self.slug])

    @property
    def view_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="400">')

    class Meta:
        # "-MODEL_COLUMN" => ordem decrescente/ "MODEL_COLUMN" => ordem crescente
        ordering = ("-published",)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.title}"


@receiver(pre_save, sender=BlogPost)
def insert_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)


@receiver(pre_save, sender=Category)
def insert_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
