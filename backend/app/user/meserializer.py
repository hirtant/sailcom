from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..booking.serializers import BookingSerializer

User = get_user_model()


class MeSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(read_only=True, many=True)
    membership_type = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = User
        fields = ['id', 'salutation', 'email', 'first_name', 'last_name', 'street', 'address_appendix', 'city',
                  'country', 'zip_code', 'phone', 'mobile', 'date_of_birth', 'licence', 'joined', 'avatar',
                  'licence_ok', 'entry_fee_paid', 'bookings', 'is_member', 'membership_type', 'request_membership',
                  'instructed_for_models', 'favourite_lake', 'is_crew', 'is_staff']
        read_only_fields = ['instructed_for_models']
