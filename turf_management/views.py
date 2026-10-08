from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from turf_management.serializer import UserSerializers,TurfSerializer
from turf_management.models import Turf

# Create your views here.
class AdminRegister(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instants = UserSerializers(data=form_data)

        if serializer_instants.is_valid():

            cleeaned_data = serializer_instants.validated_data

            User.objects.create_superuser(**cleeaned_data)

            return Response(data=serializer_instants.data)

        else:

            return Response(data=serializer_instants.errors)


class TurfListCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes  = [permissions.IsAdminUser]

    def get(slef,request):

        qs = Turf.objects.all()

        serializers_instatns = TurfSerializer(qs,many=True)

        return Response(data=serializers_instatns.data)

    def post(self,request):

        form_data = request.data

        serializer_instants = TurfSerializer(data=form_data)

        if serializer_instants.is_valid():

            cleened_data = serializer_instants.validated_data

            Turf.objects.create(**cleened_data)

            return Response(data=serializer_instants.data)

        else:
            return Response(data=serializer_instants.errors)

class TurfRetrieveUpdateDeleteView(APIView):
    """
        authentication_classes = [authentication.BasicAuthentication]
        
        permission_classes  = [permissions.IsAdminUser]"""

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_instatnt = TurfSerializer(qs)

        return Response(data=serializer_instatnt.data) 

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instant = TurfSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleened_data = serializer_instant.validated_data

            Turf.objects.filter(id=pk).update(**cleened_data)

            return Response(data=serializer_instant.data)

        else:
            return Response(data=serializer_instant.errors)

    def delete(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serialiser_instants = TurfSerializer(qs)

        qs.delete()

        return Response(data=serialiser_instants.data)    