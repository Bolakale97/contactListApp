import pyjwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        
        prefix,token = auth_data.decode('utf-8').split(' ', maxsplit=1)

        try:
            payload = pyjwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])

            user = User.objects.get(username=payload['username'])
            return (user, token)

        except pyjwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(f"Your token is invalid,login {str(identifier)}")
        except pyjwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is expired,login')
        
        return super().authenticate(request)
