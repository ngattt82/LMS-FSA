from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Chat, User

def user_list_view(request):
    # List all users
    users = User.objects.all()
    return render(request, 'chat/user_list.html', {'users': users})

def chat_view(request, username):
    other_user = get_object_or_404(User, username=username)
    users_sent_to_receiver = User.objects.filter(
        id__in=Chat.objects.filter(receiver=other_user).values('sender')
    )

    sender_name = request.GET.get('sender', None)
    sender = get_object_or_404(User, username=sender_name) if sender_name else None

    if sender:
        messages = Chat.objects.filter(
            (Q(sender=sender) & Q(receiver=other_user)) | 
            (Q(sender=other_user) & Q(receiver=sender))
        ).order_by('timestamp')
    else:
        messages = Chat.objects.filter(receiver=other_user).order_by('timestamp')

    if request.method == "POST":
        message_text = request.POST.get('message', '')
        selected_sender = request.POST.get('sender', None)
        selected_receiver = request.POST.get('receiver', None)
        sender = get_object_or_404(User, username=selected_sender) if selected_sender else None
        receiver = get_object_or_404(User, username=selected_receiver) if selected_receiver else None
        if sender and receiver and message_text:
            Chat.objects.create(sender=sender, receiver=receiver, message=message_text)
            return redirect('chat:chat_view', username=sender.username)

    users = User.objects.exclude(username=request.user.username)

    context = {
        'other_user': other_user,
        'users_sent_to_receiver': users_sent_to_receiver,
        'messages': messages,
        'sender': sender,
        'users': users
    }
    return render(request, 'chat/chat_view.html', context)


def send_message_form(request):
    if request.method == "POST":
        recipient_username = request.POST.get('recipient')
        message_text = request.POST.get('message')
        sender_username = request.POST.get('sender')  # Assume sender is passed from the form
        recipient = get_object_or_404(User, username=recipient_username)
        sender = get_object_or_404(User, username=sender_username)
        if recipient and sender and message_text:
            Chat.objects.create(sender=sender, receiver=recipient, message=message_text)
            return redirect('chat:chat_view', username=recipient_username)  # Corrected redirect
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'chat/send_message_form.html', context)