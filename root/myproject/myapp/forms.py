from django import forms
from .models import Room_Details,CustomUser



class Room_Details_Form(forms.ModelForm):
	class Meta:
		model=Room_Details
		fields='__all__'
		exclude=['owner',]

class SignUpForm(forms.ModelForm):
	class Meta:
	 model=CustomUser
	 fields=['username','first_name','last_name','email','contact_number','password']


		