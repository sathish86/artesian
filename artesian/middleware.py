import re

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
EXEMPT_URLS += [re.compile(rec) for rec in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Middleware used to check user authentication before allowing to view
        :param request: django request object
        :param view_func: view function that needs to be called
        :param view_args: argument for view
        :param view_kwargs: keyword argument for view
        :return: redirect url
        """
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        is_url_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('integrator:logout').lstrip('/'):
            logout(request)

        if request.user.is_authenticated() and is_url_exempt:
            # user already and logged in and trying to access login or registration page,
            # then they have to redirected to home page.
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated() or is_url_exempt:
            return None

        else:
            return redirect(settings.LOGIN_URL)
