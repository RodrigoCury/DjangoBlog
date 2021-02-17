from django.contrib import admin
from .models import BlogPost

# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", "author", "status")
    list_filter = ('status', "created", "published", "author")
    date_hierarchy = "published"
    raw_id_fields = ("author",)
    search_fields = ('title', "content")
    prepopulated_fields = {
        "slug": ("title",)
    }

    """
        STATUS = (
        ('rascunho', "Rascunho"),
        ('publicado', "Publicado")
    )  # tuple of dual tuples
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

    """
