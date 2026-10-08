from django.contrib.auth.models import User

from rest_framework import serializers

from booking_v2.models import Booking


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class TurfBookingSerializer(serializers.ModelSerializer):

    booking_time = serializers.TimeField(read_only=True)

    class Meta:
        
        model = Booking

        fields = '__all__'

        read_only_fields = ["id", "booking_time"]

class TurfBookingSerializer(serializers.ModelSerializer):

    turf = serializers.StringRelatedField()

    class Meta:

        model = Booking

        fields = '__all__'

        read_only_fields = ["id", "booking_time"]

    def validate(self, validate_data):

        turf = validate_data.get("turf")
        booking_date = validate_data.get("booking_date")

        if not turf:
            raise serializers.ValidationError("Turf is required.")

        if not booking_date:
            raise serializers.ValidationError("Booking date is required.")

        return validate_data

        