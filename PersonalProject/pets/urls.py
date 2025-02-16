from django.urls import path

from PersonalProject.pets import views
from PersonalProject.pets.views import PetProfileDetailView, DashboardView, edit_pet_profile, \
    delete_pet_profile, request_pet_care, respond_to_pet_care_request, my_requests

urlpatterns = [
    path('create/', views.create_pet_profile, name='create-pet-profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', PetProfileDetailView.as_view(), name='pet-profile-details'),
    path('edit-pet/<int:pet_id>/', edit_pet_profile, name='edit-pet-profile'),
    path('delete-pet/<int:pet_id>/', delete_pet_profile, name='delete-pet-profile'),
    path('request-pet-care/<int:pet_id>/', request_pet_care, name='request-pet-care'),
    path('respond-pet-care/<int:request_id>/<str:action>/', respond_to_pet_care_request, name='respond-pet-care'),
    path('my-requests/', my_requests, name='my-requests'),

]