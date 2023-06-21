import os

import jwt

from django.conf import settings
from django.contrib.auth.models import User
from dotenv import load_dotenv
from rest_framework import authentication, exceptions, status
from rest_framework.response import Response

from users.models import Users


load_dotenv()


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if not request.headers.get('Authorization'):
            return None
        authorization = request.headers.get('Authorization')
        _, token = authorization.split(' ')
        try:
            token_decode = jwt.decode(token, key=settings.SECRET_KEY, algorithms=[os.getenv('ALGORITHM')])
        except Exception:
            raise SyntaxError('Invalid token')
        user_id = token_decode['user_id']
        try:
            user = Users.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
