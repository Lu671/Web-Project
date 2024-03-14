from django.shortcuts import render
# Create your views here.

def home(request):
# render the appropriate template for this request
    return render(request,'home.html')


def addEvent(request):
    return render(request,'AddEvent.html')

def listEvents(request):
    events = [
        {'title': 'Event 1', 'date': '2024-03-15', 'description': 'Tech workshop', 'location':'Computer College',
        'agenda':'media\Event 1 Agenda.pdf'},
        {'title': 'Event 2', 'date': '2024-04-15', 'description': 'Programming Competition',
        'location':'Computer College','agenda':'media\Event 2 Agenda.pdf'},
    ]
    context = {'events': events}
    return render(request, 'EventsList.html', context)


 
