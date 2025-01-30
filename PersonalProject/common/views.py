
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "common/home-page.html"


class AboutView(TemplateView):
    template_name = "common/about-us.html"


