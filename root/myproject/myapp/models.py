from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator ,MinValueValidator,RegexValidator




     
class Room_Details(models.Model):

     category=[('single_room','Single Room'),('double_room','Double Room'),('1bk','1BK'),('1bhk','1BHK'),('2bk','2BK'),('2bhk','2BHK'),('3bk','3BK'),('3bhk','3BHK')]
     room_category=models.CharField(max_length=50,choices=category)
     rent=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000000)],help_text="Rent per Month")
     city=models.CharField(max_length=50)
     location=models.CharField(max_length=100)
     image=models.ImageField(upload_to='room_images/',null=True,blank=True)
     owner=models.ForeignKey('CustomUser',on_delete=models.CASCADE,null=True,blank=True)



class CustomUser(AbstractUser):
     contact_number=models.CharField(max_length=15,validators=[RegexValidator(r'^(\+977)?9[78]\d{8}$',message="Enter a valid phone number ")])
     email_verified=models.BooleanField(default=False)


     

     



