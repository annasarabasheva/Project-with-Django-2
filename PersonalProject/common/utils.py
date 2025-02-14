from calendar import HTMLCalendar
from django.urls import reverse
from PersonalProject.common.models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super().__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        event_html = ''.join(f'<li>{event.get_html_url}</li>' for event in events_per_day)

        if day != 0:
            add_event_url = reverse('event-new') + f"?date={self.year}-{self.month:02d}-{day:02d}"
            return f"""
            <td>
                <a href="{add_event_url}" class="date">{day}</a>
                <ul>{event_html}</ul>
            </td>
            """
        return '<td></td>'

    def formatweek(self, theweek, events):
        return f'<tr>{" ".join(self.formatday(d, events) for d, _ in theweek)}</tr>'

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal