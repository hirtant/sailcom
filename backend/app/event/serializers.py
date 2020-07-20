from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Event
from ..user.serializers import UserSerializer

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    num_participants = serializers.SerializerMethodField(required=False)

    def get_num_participants(self, event):
        return User.objects.filter(participated_events=event).count()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'price', 'created', 'updated',
                  'from_date_time', 'until_date_time', 'meeting_point',
                  'boat_model', 'event_type', 'instructor', 'participants',
                  'boat', 'max_participants', 'num_participants']
