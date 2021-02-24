from django.contrib import admin
from .models import BlogPost, Category

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
    content = models.TextField(verbose_name='Conteúdo',)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="rascunho")
    """


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'created_at')
    list_filter = ('name', 'published', 'created_at')
    date_hierarchy = 'published'
    search_fields = ('name', )
    '''
        name = models.CharField(max_length=100,
                            verbose_name='Nome')
        published = models.DateTimeField(default=timezone.now)
        created_at = models.DateTimeField(auto_now_add=True)
    '''
