from django import forms
from django.contrib.auth import get_user_model

from PersonalProject.pets.models import PetProfile, PetCareRequest

UserModel = get_user_model()


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


class PetCareRequestForm(forms.ModelForm):
    class Meta:
        model = PetCareRequest
        fields = ['caregiver', 'start_date', 'end_date', 'message']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['caregiver'].queryset = UserModel.objects.filter(profile__is_caregiver=True).exclude(id=user.id)

