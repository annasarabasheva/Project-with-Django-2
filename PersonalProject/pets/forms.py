from django import forms

from PersonalProject.pets.models import PetProfile


class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['name', 'age', 'breed', 'weight', 'photo', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age in Years'}),
            'breed': forms.TextInput(attrs={'placeholder': 'Breed'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Weight in kg'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your pet'}),
            'photo': forms.TextInput(attrs={'placeholder': 'Photo URL'}),
        }
        labels = {
            'photo': 'Photo URL of your pet',
        }