from api.models import User, Event, Attendee, File, Reaction
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class EventSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Event
        fields = ['id', 'creator', 'description', 'picture', 'location']

class EventCreateSerializer(EventSerializer):
    creator = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        write_only=False
    )

class AttendeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Attendee
        fields = ['id', 'user']


class AttendeeCreateSerializer(AttendeeSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        write_only=False
    )
    event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        required=False,
        write_only=False
    )

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'event', 'file_location']

class ReactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    event = EventSerializer()

    class Meta:
        model = Reaction
        fields = ["id", "user", "event", "type", "message", "availibility_date", "created_at"]

class ReactionCreateSerializer(ReactionSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        write_only=False
    )
    event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        required=False,
        write_only=False
    )