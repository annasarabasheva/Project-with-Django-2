from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from PersonalProject.pets.forms import PetProfileForm


@login_required
def create_pet_profile(request):
    if request.method == 'POST':
        form = PetProfileForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('home')  #Redirect to a dashboard or pet list but for now to home until we have the dashboard
    else:
        form = PetProfileForm()
    return render(request, 'pets/create-pet-profile.html', {'form': form})