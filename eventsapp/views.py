from django.shortcuts import render
# Create your views here.

def home(request):
# render the appropriate template for this request
    return render(request,'home.html')


def addEvent(request):
    return render(request,'AddEvent.html')

def listEvents(request):
    return render(request,'EventsList.html')


 
