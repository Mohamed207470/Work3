"""management_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api import views
#from mt import views
from mt.views import ProjectCreate, TaskCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    #path('signup/', views.signupuser, name='signup'),
    #path('login/', views.loginuser, name='loginuser'),
    #path('logout/', views.logoutuser, name='logoutuser'),

    #path('create_project/', ProjectCreate.as_view()),
    #path('create_task/', TaskCreate.as_view()),
    path('api/projects', views.ProjectListCreate.as_view()),
    path('api/tasks',views.TaskListCreate.as_view()),
    path('api/tasks/<int:pk>', views.TaskRetrieveUpdateDestroy.as_view()),
    path('api/projects/<int:pk>', views.ProjectRetrieveUpdateDestroy.as_view()),
    path('api-auth/', include('rest_framework.urls')),
              ]
