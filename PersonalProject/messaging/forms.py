from django import forms

from PersonalProject.messaging.models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ["text"]