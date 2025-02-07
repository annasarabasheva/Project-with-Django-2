from django.contrib.auth.views import LogoutView
from django.urls import path
from PersonalProject.accounts.views import AppUserLoginView, AppUserRegisterView, user_profile, edit_profile, \
    delete_profile

urlpatterns = [
    path('login/', AppUserLoginView.as_view(), name='login'),
    path('register/', AppUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='user-profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('delete-profile/', delete_profile, name='delete-profile'),

]