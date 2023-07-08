from django.urls import path
from . import views 

urlpatterns = [
    path('rooms/', views.projectRooms, name='projectrooms'),
    path('rooms/<str:pk>', views.projectRoom, name='projectroom'),
    path('create-room/', views.createRoom, name='createroom'),
    path('update-room/<str:pk>', views.updateRoom, name='updateroom'),
    path('delete-room/<str:pk>', views.deleteRoom, name='deleteroom'),
    path('delete-message/<str:pk>', views.deleteMessage, name='deletemessage'),
]