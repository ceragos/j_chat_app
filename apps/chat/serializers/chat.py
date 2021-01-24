from rest_framework import serializers

from apps.chat.models import Message


class MessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'content', 'created']
