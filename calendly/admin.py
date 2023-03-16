from django.contrib import admin
from .models import Appointment

#admin.site.register(Appointment)
@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','contact','appointment','date','stime']