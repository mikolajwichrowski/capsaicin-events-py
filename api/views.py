from django.shortcuts import get_object_or_404

from api.serializers import UserSerializer, EventSerializer, EventCreateSerializer, AttendeeSerializer, AttendeeCreateSerializer, FileSerializer, ReactionSerializer, ReactionCreateSerializer
from api.models import User, Event, Attendee, File, Reaction

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.response import Response
from api.auth import Protected
from rest_framework.decorators import action


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
        return Response(serializer.data, status=201)
    
    @action(methods=['GET'], detail=True, url_path='attendees')
    def list_attendees(self, request, pk):
        attendees = Attendee.objects.filter(event_id=pk)
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)
    
    @action(methods=['POST'], detail=True, url_path='register')
    def register_attendee(self, request, pk):
        request.data["event"] = pk
        serializer = AttendeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(methods=['GET'], detail=True, url_path='files')
    def list_event_files(self, request, pk):
        serializer = FileSerializer(File.objects.filter(event_id=pk), many=True)
        return Response(serializer.data)
    
    @action(methods=['POST'], detail=True, url_path='upload')
    def upload_event_file(request, pk):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        file_location = f"media/{file_uploaded.name}"
        with open(file_location, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        data = {
            event: int('pk'),
            file_location: f"/{file_location}"
        }
        serializer = FileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    @action(methods=['GET'], detail=True, url_path='reactions')
    def list_reactions(self, request, pk):
        reactions = Reaction.objects.filter(event_id=pk)
        serializer = ReactionSerializer(reactions, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True, url_path='react')
    def upload_event_file(request, pk):
        data = {
            **request.data,
            event: int('pk'),
            user: request.COOKIES["user_id"]
        }
        serializer = ReactionCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    







