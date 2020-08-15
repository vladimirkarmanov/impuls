from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
        labels = {'text': ''}

        widgets = {
            'text': forms.TextInput(attrs={'class': 'write_msg',
                                           'placeholder': 'Сообщение'})
        }
