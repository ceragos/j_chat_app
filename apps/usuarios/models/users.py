from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_online = models.BooleanField(default=False)

    def set_online(self):
        self.is_online = True
        self.save()

    def set_offline(self):
        self.is_online = False
        self.save()
