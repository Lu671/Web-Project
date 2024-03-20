from django.shortcuts import render,redirect
from .models import Events

def home(request):
# render the appropriate template for this request
    return render(request,'home.html')


def addEvent(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description')
        location = request.POST.get('location')
        
        event = Events(title=title, date=date, description=description, location=location)
        event.save()
        
        return redirect('listEvents')  # Redirect to the event list page
    else:
        return render(request, 'AddEvent.html')

def listEvents(request):
    old_events = [
    {'title': 'Event 1', 'date': '2024-03-15', 'description': 'Tech workshop', 'location':'Computer College','agenda':'media\Event 1 Agenda.pdf'},
    {'title': 'Event 2', 'date': '2024-04-15', 'description': 'Programming Competition','location':'Computer College','agenda':'media\Event 2 Agenda.pdf'},
    ]
    events = Events.objects.all()
    context = {'events': events, 'old_events': old_events}
    return render(request, 'EventsList.html', context)
   


 
