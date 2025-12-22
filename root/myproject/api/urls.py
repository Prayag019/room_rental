from django.urls import path
from .views import List_Create_Rooms,List_Create_User


urlpatterns=[

path('rooms/',List_Create_Rooms.as_view(),name='get-create-rooms'),
path('signup-form/',List_Create_User.as_view(),name='get-create-user-form'),



]


