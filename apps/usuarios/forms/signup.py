from django.contrib.auth.forms import UserCreationForm, UsernameField

from apps.usuarios.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
