from django.views.generic import TemplateView
from rest_framework import viewsets, mixins
from rest_framework.viewsets import ModelViewSet

from apps.chat.models import Message
from apps.chat.serializers import MessageModelSerializer
from apps.usuarios.models import User


class ChatTemplateView(TemplateView):
    template_name = 'chat/chat.html'

    def get_context_data(self, **kwargs):
        context = super(ChatTemplateView, self).get_context_data()
        context['users'] = self.get_all_users_on_line()
        context['messages'] = self.get_all_messages()
        return context

    def get_all_users_on_line(self):
        users = User.objects.filter(is_online=True).exclude(pk=self.request.user.pk)
        return users

    def get_all_messages(self):
        messages = Message.objects.all()
        return messages


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer
