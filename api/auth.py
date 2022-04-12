from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer
from api.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from enum import Enum


class CookieKeys(Enum):
    logged_in = "logged_in"
    user_id = "user_id"


class Protected(BasePermission):
    def has_permission(self, request, _):
        print(request.COOKIES)
        is_logged_in = request.COOKIES.get(CookieKeys.logged_in.value)

        if is_logged_in != "yes":
            return False
        try:
            user_id = request.COOKIES.get(CookieKeys.user_id.value)
            user_object = User.objects.get(pk=int(user_id))
            if user_object:
                return True
        except Exception as e:
            print(f"{e.args[0]}")
            pass
        return False


@api_view(['POST'])
def authenticate(request):
    payload = request.data
    try:
        user_logging_in = User.objects.get(
            username=payload.get("username"), password=payload.get("password"))
        cookie_response = Response("")
        cookie_response.set_cookie(CookieKeys.logged_in.value, 'yes')
        cookie_response.set_cookie(
            CookieKeys.user_id.value, user_logging_in.id)
        return cookie_response
    except:
        return Response(status=403)


@api_view(['POST'])
def register(request):
    payload = request.data
    try:
        new_user = User.objects.create(
            username=payload.get("username"), password=payload.get("password"))
        cookie_response = Response({
            "id": new_user.id,
            "username": new_user.username
        })
        cookie_response.set_cookie(CookieKeys.logged_in.value, 'yes')
        cookie_response.set_cookie(CookieKeys.user_id.value, new_user.id)
        return cookie_response
    except Exception as e:
        return Response(data=f"{e.args[0]}", status=500)
