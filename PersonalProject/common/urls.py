from django.urls import path
from PersonalProject.common.views import HomeView, AboutView, contact_us, faq, CalendarView, event

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact_us, name='contact-us'),
    path("faq/", faq, name="faq"),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('calendar/event/', event, name='event-new'),
    path('calendar/event/edit/<int:event_id>/', event, name='event-edit'),
]

