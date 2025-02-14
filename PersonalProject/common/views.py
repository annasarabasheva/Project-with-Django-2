import calendar
from datetime import timedelta, datetime

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe
from django.views import generic
from django.views.generic import TemplateView

from PersonalProject.common.forms import EventForm
from PersonalProject.common.models import Event
from PersonalProject.common.utils import Calendar


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


class CalendarView(generic.ListView):
    model = Event
    template_name = 'common/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        month_str = self.request.GET.get('month', None)
        d = get_date(month_str)

        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)

        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context


def get_date(req_day):
    if req_day:
        try:
            year, month = (int(x) for x in req_day.split('-'))
            return datetime(year, month, 1).date()
        except ValueError:
            return datetime.today().date()
    return datetime.today().date()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    return f"month={prev_month.year}-{prev_month.month:02d}"


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    return f"month={next_month.year}-{next_month.month:02d}"


def event(request, event_id=None):
    instance = get_object_or_404(Event, pk=event_id) if event_id else Event()

    selected_date = request.GET.get('date', None)
    if selected_date and not event_id:
        try:
            instance.start_time = datetime.strptime(selected_date, "%Y-%m-%d")
            instance.end_time = instance.start_time
        except ValueError:
            pass

    form = EventForm(request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('calendar')

    return render(request, 'common/event.html', {'form': form})