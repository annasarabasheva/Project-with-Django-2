from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from PersonalProject.pets.forms import PetProfileForm, PetCareRequestForm
from PersonalProject.pets.models import PetProfile, PetCareRequest


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


@login_required
def request_pet_care(request, pet_id):
    pet = get_object_or_404(PetProfile, id=pet_id)

    if request.method == "POST":
        form = PetCareRequestForm(request.POST)
        if form.is_valid():
            pet_care_request = form.save(commit=False)
            pet_care_request.owner = request.user
            pet_care_request.pet = pet
            pet_care_request.save()
            return redirect("my-requests")

    else:
        form = PetCareRequestForm()

    return render(request, "pets/request-pet-care.html", {"form": form, "pet": pet})


@login_required
def respond_to_pet_care_request(request, request_id, action):
    pet_care_request = get_object_or_404(PetCareRequest, id=request_id, caregiver=request.user)

    if action == "accept":
        pet_care_request.status = "Accepted"
    elif action == "decline":
        pet_care_request.status = "Declined"

    pet_care_request.save()
    return redirect("my-requests")


@login_required
def my_requests(request):
    sent_requests = PetCareRequest.objects.filter(owner=request.user)
    received_requests = PetCareRequest.objects.filter(caregiver=request.user)

    return render(request, "pets/my-requests.html", {
        "sent_requests": sent_requests,
        "received_requests": received_requests,
    })