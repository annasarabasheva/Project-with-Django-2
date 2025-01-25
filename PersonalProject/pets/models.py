from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class PetProfile(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    weight = models.FloatField()
    photo = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.breed})"