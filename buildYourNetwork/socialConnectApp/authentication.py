import jwt
import datetime 
from rest_framework import exceptions
from rest_framework.permissions import BasePermission

class IsAuthenticatedCustom(BasePermission):
    def has_permission(self, request, view):
        return request.user is not None and request.user.is_authenticated

def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload, 'secret', algorithm='HS256')

def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('Invalid token')
    
def generate_refresh_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow()
    }
    return jwt.encode(payload, 'secret', algorithm='HS256')

def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('Invalid token')
    