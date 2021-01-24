from django.contrib.auth import logout
from django.views.generic import RedirectView


class LogoutView(RedirectView):
    pattern_name = 'usuario:login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
