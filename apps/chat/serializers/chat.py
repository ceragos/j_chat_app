from rest_framework import serializers

from apps.chat.models import Message


class MessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'content', 'image', 'created']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['username'] = instance.user.get_username()
        data['username_encrypt_md5'] = instance.user.get_username_encrypt_md5
        data['owner'] = instance.user == self.context.get("request").user
        return data
