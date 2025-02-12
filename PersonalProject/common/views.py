from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "common/home-page.html"


class AboutView(TemplateView):
    template_name = "common/about-us.html"


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        messages.success(request, "Your message has been sent!")

    return render(request, "common/contact-us.html")


def faq(request):
    faqs = [
        {"question": "How do I request pet care?", "answer": "Go to a pet profile and click 'Request Pet Care'."},
        {"question": "Can I edit my pet’s profile?", "answer": "Yes, go to 'My Pets' and click 'Edit' on your pet's profile."},
        {"question": "How do I delete my profile?", "answer": "You can delete your profile from the 'Edit Profile' page."},
        {"question": "How can I contact support?", "answer": "Use the 'Contact Us' page to send us a message."},
    ]
    return render(request, "common/faq.html", {"faqs": faqs})