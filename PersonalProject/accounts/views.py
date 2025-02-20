from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from PersonalProject.accounts.forms import AppUserCreationForm, ProfileEditForm, CaregiverSignupForm, RatingForm
from PersonalProject.accounts.models import Profile, Rating
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

        login(self.request, self.object)

        return response


@login_required
def user_profile(request):
    pets = PetProfile.objects.filter(owner=request.user)
    return render(request, "accounts/user-profile.html", context={"pets": pets})


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


@login_required
def become_caregiver(request):
    if request.method == "POST":
        form = CaregiverSignupForm(instance=request.user.profile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("caregivers-list")
    else:
        form = CaregiverSignupForm(instance=request.user.profile)

    return render(request, "accounts/become-caregiver.html", {"form": form})


def caregivers_list(request):
    caregivers = Profile.objects.filter(is_caregiver=True).exclude(user_id__isnull=True)
    return render(request, "accounts/caregivers-list.html", {"caregivers": caregivers})


@login_required
def rate_caregiver(request, caregiver_id):
    caregiver = get_object_or_404(Profile, user_id=caregiver_id, is_caregiver=True)
    reviews = Rating.objects.filter(caregiver=caregiver).order_by('-created_at')

    existing_rating = Rating.objects.filter(caregiver=caregiver, user=request.user).first()

    if request.method == "POST":
        form = RatingForm(request.POST, instance=existing_rating)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.caregiver = caregiver
            rating.save()
            return redirect('caregivers-list')
    else:
        form = RatingForm(instance=existing_rating)

    return render(request, "accounts/rate-caregiver.html", {
        "form": form,
        "caregiver": caregiver,
        "reviews": reviews,
    })

