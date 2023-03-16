from rest_framework import serializers
from django.contrib.auth.models import User, Group
  
# import model from models.py
from .models import Appointment
  
# Create a model serializer 
class AppSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Appointment
        fields = ('name', 'email','contact','appointment','date','stime','etime')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'