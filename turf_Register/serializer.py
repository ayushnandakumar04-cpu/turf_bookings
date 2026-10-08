from rest_framework import serializers

from turf_management.models import Turf

class TurfRegisterSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    team_name = serializers.CharField()

    phone_number = serializers.IntegerField()

    date = serializers.DateField()

    duration = serializers.CharField()