from api.models import User, Event
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class EventSerializer(serializers.HyperlinkedModelSerializer):
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
