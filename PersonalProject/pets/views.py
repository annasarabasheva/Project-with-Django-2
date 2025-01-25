from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

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
            return redirect(reverse('pet-profile-details', kwargs={'pk': pet.pk}))
    else:
        form = PetProfileForm()
    return render(request, 'pets/create-pet-profile.html', {'form': form})


class PetProfileDetailView(View):
    def get(self, request, pk):
        pet = get_object_or_404(PetProfile, pk=pk)
        return render(request, 'pets/pet-profile-details.html', {'pet': pet})