from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Booking
from ..boat.serializers import BoatSerializer
from ..user.serializers import UserSerializer


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    boat = BoatSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'boat', 'from_date_time', 'until_date_time', 'duration']

    def perform_create(self, validated_data):
        instance = Booking.objects.create(
            **validated_data
        )
        return instance


class BookingInBoatSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'from_date_time', 'until_date_time', 'duration']