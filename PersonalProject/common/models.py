from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from PersonalProject.pets.models import PetProfile

UserModel = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('event-edit', args=[self.id])
        return f'<a href="{url}">{self.title}</a>'