from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    # Caregiver-related fields
    is_caregiver = models.BooleanField(default=False)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    pet_owner = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)