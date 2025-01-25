from django.urls import path

from PersonalProject.pets import views

urlpatterns = [
    path('create/', views.create_pet_profile, name='create-pet-profile'),
]