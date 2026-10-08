from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from booking_v2.serializer import SignUpSerializer, TurfBookingSerializer
from booking_v2.models import Booking

from datetime import time
class SignUpRegisterView(APIView):

    def post (self,request):

        form_data = request.data

        serializer_instant = SignUpSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleaned_data = serializer_instant.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_instant = SignUpSerializer(user_object)

            return Response(data=serializer_instant.data)

        else:return Response(data=serializer_instant.errors)

class TurfBookingListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        qs = Booking.objects.all()

        serializer_instance = TurfBookingSerializer(qs, many=True)

        return Response(data=serializer_instance.data)

    def post(self, request):

        form_data = request.data

        serializer_instance = TurfBookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            turf = cleaned_data.get("turf")
            booking_date = cleaned_data.get("booking_date")

            bookings = Booking.objects.filter(turf=turf,booking_date=booking_date).order_by("booking_time")

            if not bookings.exists():

                booking_time_details = time(10, 0)

            elif bookings.count() == 1:

                booking_time_details = time(12, 0)

            else:

                return Response({
                    "Message": "No booking slots available for this date."
                })

            booking_object = Booking.objects.create(
                **cleaned_data,
                booking_time=booking_time_details
            )

            serializer_instant = TurfBookingSerializer(booking_object)

            return Response(data=serializer_instant.data)

        else:

            return Response(data=serializer_instance.errors)