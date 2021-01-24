from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('chat:home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        self.request.user.set_online()
        return super(LoginView, self).form_valid(form)
