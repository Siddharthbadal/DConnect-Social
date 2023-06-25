from django.urls import path, include
from . import views 


urlpatterns = [
   
    path('', views.projects, name='projects'),
    path('project/<str:pk>', views.project, name='project'),
    path('create_project/', views.createProject, name='createProject'),
    path('update_project/<str:pk>', views.updateProject, name='updateProject'),
    path('delete_project/<str:pk>', views.deleteProject, name='deleteProject'),
]
