from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from myapp.models import Room_Details,CustomUser
from .serializers import Room_Details_Serializer,SignUpForm_Serializer





class List_Create_Rooms(ListCreateAPIView):
    queryset=Room_Details.objects.all()
    serializer_class=Room_Details_Serializer

class List_Create_User(ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=SignUpForm_Serializer





