from myapp.models import Room_Details,CustomUser
from rest_framework import serializers


class Room_Details_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Room_Details
		
		exclude=['owner']


class SignUpForm_Serializer(serializers.ModelSerializer):
    class Meta:
       model=CustomUser
       fields="__all__"

       
		




