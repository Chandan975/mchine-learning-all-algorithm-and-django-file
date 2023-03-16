from django.db import models
from pytz import timezone



class Appointment(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    contact= models.CharField(max_length=30)
    appointment=models.CharField(max_length=30)
    date= models.DateTimeField(auto_now_add=True)
    stime = models.TimeField()
    etime= models.TimeField()






    
   



