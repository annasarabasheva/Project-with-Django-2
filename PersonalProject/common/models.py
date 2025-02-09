from django.db import models
from django.contrib.auth import get_user_model

from PersonalProject.pets.models import PetProfile

UserModel = get_user_model()


class PetCareRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Completed', 'Completed'),
    ]

    pet = models.ForeignKey(PetProfile, on_delete=models.CASCADE, related_name="care_requests")
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="requests_sent")
    caregiver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="requests_received")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pet.name} - {self.status}"
