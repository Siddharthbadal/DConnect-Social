from django.urls import path
from . import views 


urlpatterns = [
   
    path('', views.profiles, name='profiles'),

    path('profile/<str:pk>', views.userProfile, name='userprofile'),
    
    path('login/', views.userLogin, name='userlogin'),
    path('logout/', views.userLogOut, name='userlogOut'),
    path('register/', views.userRegister, name='userregister'),
    path('account/', views.userAccount, name='useraccount'),

    path('updateAccount/', views.update_account, name='updateaccount'),
    path('create-skills/', views.createSkills, name='createSkills' ),
    path('update-skills/<str:pk>', views.updateSkills, name='updateskills'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='deleteskill'),
    path('inbox/', views.inbox, name='inbox'),
    path('view-message/<str:pk>', views.viewMessage, name='viewmessage'),
    path('send-message/<str:pk>/', views.createMessage, name='createmessage'),

]
