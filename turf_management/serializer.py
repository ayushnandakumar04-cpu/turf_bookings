from rest_framework import serializers

from turf_management.models import Turf

class TurfSerializer(serializers.ModelSerializer):

    class Meta:

        model =Turf
        fields = '__all__'


class UserSerializers(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()