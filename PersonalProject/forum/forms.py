from django import forms

from PersonalProject.forum.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']