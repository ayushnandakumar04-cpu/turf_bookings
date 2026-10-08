from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from turf_Register.models import TurfRegister

from turf_Register.serializer import TurfRegisterSerializer
# Create your views here.

class TurfRegisterListCreate(APIView):

    def get(self,request):

        qs = TurfRegister.objects.all()

        serializer_instants = TurfRegisterSerializer(qs,many=True)

        return Response(data=serializer_instants.data)

    def post(self,request):

        form_data = request.data

        serializer_instant = TurfRegisterSerializer(data=form_data)

        if serializer_instant.is_valid():

            cleened_data = serializer_instant.validated_data

            TurfRegister.objects.create(**cleened_data)

            return Response(data=serializer_instant.data)

        else:
            return Response(data=serializer_instant.errors)

class TurfRetrieveUpdateDelete(APIView):

    def get (self,request,pk=None):

        qs = TurfRegister.objects.get(id=pk)  

        serializer_instant = TurfRegisterSerializer(qs)  

        return Response(data=serializer_instant.data)  

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instant = TurfRegisterSerializer(data= form_data)

        if serializer_instant.is_valid():

            cleeaned_data = serializer_instant.validated_data

            TurfRegister.objects.filter(id=pk).update(**cleeaned_data)

            return Response(data=serializer_instant.data)

        else:
            return Response(data=serializer_instant.errors)  

    def delete(self,request,pk=None):

        qs = TurfRegister.objects.get(id=pk)

        serializer_instant = TurfRegisterSerializer(qs)

        qs.delete()

        return Response(data=serializer_instant.data)   