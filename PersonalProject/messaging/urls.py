from django.urls import path

from PersonalProject.messaging import views

urlpatterns = [
    path("chats/", views.chat_list, name="chat_list"),
    path("chat/<int:room_id>/", views.chat_room, name="chat_room"),
    path("chats/start/", views.start_chat, name="start_chat"),

]