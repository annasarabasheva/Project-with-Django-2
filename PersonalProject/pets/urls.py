from django.urls import path

from PersonalProject.pets import views
from PersonalProject.pets.views import PetProfileDetailView

urlpatterns = [
    path('create/', views.create_pet_profile, name='create-pet-profile'),
    path('profile/<int:pk>/', PetProfileDetailView.as_view(), name='pet-profile-details'),
]