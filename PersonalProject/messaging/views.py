from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from PersonalProject.messaging.forms import ChatMessageForm
from PersonalProject.messaging.models import ChatRoom


@login_required
def chat_list(request):
    chats = ChatRoom.objects.filter(Q(participant_one=request.user) | Q(participant_two=request.user))
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
def start_chat(request, user_id):
    from django.contrib.auth import get_user_model
    UserModel = get_user_model()

    other_user = get_object_or_404(UserModel, id=user_id)

    chat = ChatRoom.objects.filter(
        (Q(participant_one=request.user, participant_two=other_user) |
         Q(participant_one=other_user, participant_two=request.user))
    ).first()

    if not chat:
        chat = ChatRoom.objects.create(participant_one=request.user, participant_two=other_user)

    return redirect("chat_room", room_id=chat.id)
