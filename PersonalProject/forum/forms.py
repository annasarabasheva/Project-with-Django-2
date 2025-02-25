from django import forms

from PersonalProject.forum.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']