from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.shortcuts import render, get_object_or_404, redirect

from PersonalProject.messaging.forms import ChatMessageForm
from PersonalProject.messaging.models import ChatRoom

UserModel = get_user_model()


@login_required
def chat_list(request):
    chats = ChatRoom.objects.filter(
        Q(participant_one=request.user) | Q(participant_two=request.user)
    ).annotate(last_message_time=Max("messages__timestamp")).order_by("-last_message_time")

    return render(request, "messaging/chat-list.html", {"chats": chats})


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)

    if request.user not in [room.participant_one, room.participant_two]:
        return redirect("chat_list")

    messages = room.messages.all().order_by("timestamp")
    room.messages.filter(read=False).exclude(sender=request.user).update(read=True)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.sender = request.user
            message.save()
            return redirect("chat_room", room_id=room.id)

    else:
        form = ChatMessageForm()

    return render(request, "messaging/chat-room.html", {"room": room, "messages": messages, "form": form})


@login_required
def start_chat(request):
    users = UserModel.objects.exclude(id=request.user.id)

    if not users.exists():
        return render(request, "messaging/start-chat.html", {"users": None, "no_users": True})

    if request.method == "POST":
        selected_user_id = request.POST.get("user_id")
        selected_user = get_object_or_404(UserModel, id=selected_user_id)

        chat, created = ChatRoom.objects.get_or_create(
            participant_one=min(request.user, selected_user, key=lambda u: u.id),
            participant_two=max(request.user, selected_user, key=lambda u: u.id),
        )

        return redirect("chat_room", chat.id)

    return render(request, "messaging/start-chat.html", {"users": users, "no_users": False})

