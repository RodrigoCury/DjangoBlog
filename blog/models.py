from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    STATUS = (
        ('rascunho', "Rascunho"),
        ('publicado', "Publicado")
    )
    title = models.CharField(blank=False, max_length=50)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # Obrigatório
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="rascunho")

    class Meta:
        # "-MODEL_COLUMN" => ordem decrescente/ "MODEL_COLUMN" => ordem crescente
        ordering = ("-published",)

    def __str__(self):
        return f"{self.title} - {self.status}"
