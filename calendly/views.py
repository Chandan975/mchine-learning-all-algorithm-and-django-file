from django.shortcuts import render,HttpResponse,redirect
from calendly.models import Appointment
from .forms import AppointmentForm
from rest_framework import viewsets
from .serializers import AppSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer,AppointmentSerializer

import requests

def AddnewData(request):
    url = "http://asc.apptology.in:81/api/product/?format=json"

# Send a DELETE request to the endpoint
    response = requests.delete(url)
    print(response)

# Check the status code of the response
    if response.status_code == 204:
       return HttpResponse('Data deleted successfully')
    else:
        return HttpResponse('Failed to delete data')

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    def destroy(self, request, pk=None):
        appointment = self.get_object()
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class AppViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Appointment.objects.all()
      
    # specify serializer to be used
    serializer_class = AppSerializer

def index(request):
    
    return render(request, 'index.html')
def meeting(request):
    all_data= Appointment.objects.all()
    return render(request, 'meeting.html',{'output':all_data})
def create(request):
    try:
        if request.method=='POST':
            name= request.POST['name']
            email= request.POST['email']
            contact= request.POST['contact']
            appointment= request.POST['appointment']
            date = request.POST['date']
            stime = request.POST['stime']
            #etime = request.POST['etime']
            en= Appointment(name=name,email=email,contact=contact,appointment=appointment,date=date,stime=stime)
            en.save()
    except:
        print("wrong code")
    return render(request, 'create.html')
def availiablity(request):
    return render(request, 'availiablity.html')
def intergation(request):
    return render(request, 'intergation.html')
def rotuing(request):
    return render(request, 'rotuing.html')
def workflows(request):
    return render(request, 'workflows.html')
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

@api_view(['GET', 'POST'])
def Appointment_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Appointment.objects.all()
        serializer = AppSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def someview(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    page= p.getPageNumber()
    text="page %s" % page


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 50, text)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')