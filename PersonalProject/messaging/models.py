from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ChatRoom(models.Model):
    participant_one = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="chatroom_user1")
    participant_two = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="chatroom_user2")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.participant_one} and {self.participant_two}"


class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username}: {self.text[:30]}"