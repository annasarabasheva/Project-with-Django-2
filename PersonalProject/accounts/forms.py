from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from PersonalProject.accounts.models import Profile

UserModel = get_user_model()


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'username')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture']


class CaregiverSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "age", "bio", "experience", "pet_owner", "location"]

    pet_owner = forms.ChoiceField(
        choices=[(True, "Yes"), (False, "No")],
        widget=forms.RadioSelect,
        label="Do you have a pet?"
    )

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.is_caregiver = True
        if commit:
            profile.save()
        return profile