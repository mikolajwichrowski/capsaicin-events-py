from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer, EventSerializer, EventCreateSerializer
from api.models import User, Event

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.response import Response
from api.auth import Protected


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    permission_classes = [Protected]

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class EventViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing, retrieving or creating events.
    """
    queryset = Event.objects.all()
    permission_classes = [Protected]

    def list(self, request):
        serializer = EventSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success', 'pk': serializer.instance.pk})
