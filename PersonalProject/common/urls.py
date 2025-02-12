from django.urls import path
from PersonalProject.common.views import HomeView, AboutView, contact_us, faq

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact_us, name='contact-us'),
    path("faq/", faq, name="faq"),

]
