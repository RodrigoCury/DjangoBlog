from ckeditor.widgets import CKEditorWidget
from .models import Messages
from django import forms


class MessagesForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Nome',)
    email = forms.EmailField(label='e-Mail', )
    subject = forms.CharField(
        max_length=50, label="Assunto", required=False)
    message = forms.CharField(widget=CKEditorWidget, label='Mensagem',)

    class Meta:
        model = Messages
        fields = ('name', 'email', 'subject', 'message',)
