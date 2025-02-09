from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from PersonalProject.pets.forms import PetProfileForm
from PersonalProject.pets.models import PetProfile


@login_required
def create_pet_profile(request):
    if request.method == 'POST':
        form = PetProfileForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('dashboard')
    else:
        form = PetProfileForm()
    return render(request, 'pets/create-pet-profile.html', {'form': form})


class DashboardView(ListView):
    model = PetProfile
    template_name = 'pets/dashboard.html'
    context_object_name = 'pets'


class PetProfileDetailView(LoginRequiredMixin, DetailView):
    model = PetProfile
    template_name = 'pets/pet-profile-details.html'
    context_object_name = 'pet'


def my_pets(request):
    pets = PetProfile.objects.filter(owner=request.user)
    return render(request, 'pets/my-pets.html', {'pets': pets})


@login_required
def edit_pet_profile(request, pet_id):
    pet = get_object_or_404(PetProfile, id=pet_id, owner=request.user)

    if request.method == "POST":
        form = PetProfileForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet-profile-details", pk=pet.id)

    else:
        form = PetProfileForm(instance=pet)

    return render(request, "pets/edit-pet-profile.html", {"form": form, "pet": pet})


@login_required
def delete_pet_profile(request, pet_id):
    pet = get_object_or_404(PetProfile, id=pet_id, owner=request.user)

    if request.method == "POST":
        pet.delete()
        return redirect("my-pets")

    return render(request, "pets/delete-pet-profile.html", {"pet": pet})