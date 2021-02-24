from ckeditor.widgets import CKEditorWidget
from .models import BlogPost
from django import forms


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = BlogPost
        fields = '__all__'
