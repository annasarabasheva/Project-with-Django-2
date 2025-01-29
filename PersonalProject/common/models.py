from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Booking(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pet_name} - {self.start_time}"