from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseForbidden
from .models import User
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse
from .views import authuser_to_role

class UserAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of excluded paths
        excluded_urls = [
            '/login/',
            '/logout/',
            '/register/',
            '/admin/',
        ]

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Allow access if the request path starts with any excluded path
            if any(request.path.startswith(excluded_url) for excluded_url in excluded_urls):
                return self.get_response(request)

            # Redirect to login if not in excluded paths
            return redirect(reverse('main:login'))

        # Continue processing the request for authenticated users
        response = self.get_response(request)
        return response
class RoleMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Define URLs that are restricted
        restricted_urls = [
            '/user/users/create/',  # Example URL for adding a user
        ]
        print(f"Requested path: {request.path}")
        # Check if the requested URL is restricted
        if request.path in restricted_urls:
            user_role=authuser_to_role(request.user)
            if user_role not in ['Admin','Staff']:
                return redirect(reverse('main:home'))
            return None
        return None

