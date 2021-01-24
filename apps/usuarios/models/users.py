import hashlib

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

    @property
    def get_username_encrypt_md5(self):
        m = hashlib.md5()
        m.update(self.get_username().encode('utf-8'))
        return m.hexdigest()
