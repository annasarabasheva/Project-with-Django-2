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


