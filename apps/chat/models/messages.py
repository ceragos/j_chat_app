from django.db import models

from apps.usuarios.models import User


class Message(models.Model):
    user = models.ForeignKey(User, related_name='message_user', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ['created']
