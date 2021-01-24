from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.usuarios.forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('usuario:login')
    template_name = 'usuarios/signup.html'
