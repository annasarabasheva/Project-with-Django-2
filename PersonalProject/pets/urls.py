from django.urls import path

from PersonalProject.pets import views
from PersonalProject.pets.views import PetProfileDetailView, DashboardView, my_pets, edit_pet_profile

urlpatterns = [
    path('create/', views.create_pet_profile, name='create-pet-profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', PetProfileDetailView.as_view(), name='pet-profile-details'),
    path('my-pets/', my_pets, name='my-pets'),
    path('edit-pet/<int:pet_id>/', edit_pet_profile, name='edit-pet-profile'),

]