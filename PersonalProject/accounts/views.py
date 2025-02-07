from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from PersonalProject.accounts.forms import AppUserCreationForm, ProfileEditForm
from PersonalProject.pets.models import PetProfile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)  # Auto Login after Register

        return response


@login_required
def user_profile(request):
    return render(request, "accounts/user-profile.html")


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("user-profile")

    else:
        form = ProfileEditForm(instance=profile)

    return render(request, "accounts/edit-profile.html", {"form": form})


@login_required
def delete_profile(request):
    if request.method == "POST":
        user = request.user
        PetProfile.objects.filter(owner=user).delete()
        user.delete()
        return redirect("home")

    return render(request, "accounts/delete-profile.html")