from ckeditor.widgets import CKEditorWidget
from .models import BlogPost, Category
from django import forms


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='Título')
    category = forms.ModelMultipleChoiceField(
        label='Categoria',
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    content = forms.CharField(widget=CKEditorWidget, label='Conteúdo',)

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'category', 'image', 'status')
