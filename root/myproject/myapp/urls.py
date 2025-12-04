from django.urls import path
from .views import Room_Form_View,User_Information,Login_Form,Homepage
urlpatterns =[
path('detail-form/',Room_Form_View,name='room-form'),
path('user-information/',User_Information,name='user-information-form'),

path('login-form/',Login_Form,name='login-form'),
path('homepage/',Homepage,name='home-page')



]