"""project22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from calendly import views
from rest_framework import routers
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
router = routers.DefaultRouter()
router.register(r'app', views.AppViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('snippets/', views.Appointment_list),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('a', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('AddnewData/', views.AddnewData, name='AddnewData'),
    path('meeting/', views.meeting, name='meeting'),
    path('create/', views.create, name='create'),
    path('availiablity/', views.availiablity, name='availiablity'),
    path('intergation/', views.intergation, name='intergation'),
    path('rotuing/', views.rotuing, name='rotuing'),
    path('workflows/', views.workflows, name='workflows'),
    path('someview/', views.someview, name='someview'),

   
    
]
