from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from register.models import User
from chats.forms import MessageForm
from chats.models import Chat


class ChatsView(LoginRequiredMixin, View):
    template = 'chats/chats.html'

    def get(self, request):
        chats = Chat.objects \
            .annotate(msg_count=Count('messages')) \
            .filter(members__in=[request.user.id], msg_count__gt=0)
        return render(request,
                      self.template,
                      {'chats': chats})


class MessagesView(LoginRequiredMixin, View):
    template = 'chats/messages.html'

    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.messages.unreaded().exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
            request,
            self.template,
            {'user_profile': request.user,
             'chat': chat,
             'form': MessageForm()}
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('chats:messages', kwargs={'chat_id': chat_id}))


class CreateChatView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.filter(id=user_id).first()
        if user == request.user:
            return redirect(reverse('chats:dialogs'))
        chats = Chat.objects \
            .filter(members__in=[request.user.id, user_id], type=Chat.DIALOG) \
            .annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user)
        else:
            chat = chats.first()
        return redirect(reverse('chats:messages', kwargs={'chat_id': chat.id}))
