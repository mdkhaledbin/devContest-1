from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from .authentication import decode_access_token
from django.contrib.auth.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('access_token')  # Get JWT from cookies
        if not token:
            return None

        try:
            # print(token)
            user_id = decode_access_token(token)
            user = User.objects.get(id=user_id)
            return (user, None)  # Return user and token
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired token")