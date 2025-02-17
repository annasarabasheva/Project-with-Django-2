from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg

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

    def average_rating(self):
        return self.ratings.aggregate(Avg('rating'))['rating__avg'] or 0

    def review_count(self):
        return self.ratings.count()


class Rating(models.Model):
    caregiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('caregiver', 'user')
    def __str__(self):
        return f"{self.user.username} → {self.caregiver.first_name}: {self.rating}⭐"