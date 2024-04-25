from django.shortcuts import render,redirect
from .models import Events
from .forms import EventForm

def home(request):
# render the appropriate template for this request
    return render(request,'home.html')


def addEvent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            
            event = Events(title=title, date=date, description=description, location=location)
            event.save()
            
            return redirect('listEvents')  # Redirect to the event list page
    else:
        form = EventForm()

    return render(request, 'AddEvent.html', {'form': form})

def listEvents(request):
    month_names = {1: 'January',2: 'February',3: 'March',4: 'April',5: 'May',
                   6: 'June',7: 'July',8: 'August',9: 'September',10: 'October',
                   11: 'November',12: 'December'}
    old_events = [
    {'title': 'Event 1', 'date': '2024-03-15', 'description': 'Tech workshop', 'location':'Computer College','agenda':'media\Event 1 Agenda.pdf'},
    {'title': 'Event 2', 'date': '2024-04-15', 'description': 'Programming Competition','location':'Computer College','agenda':'media\Event 2 Agenda.pdf'},
    ]
    selected_month = request.GET.get('month')
    month_name = month_names.get(int(selected_month)) if selected_month else None
    if selected_month:
        events = Events.objects.filter(date__month=selected_month).order_by('date') # order_by
        num_events = events.count() #count
        context = {'events': events, 'month':month_name, 'old_events': old_events, 'num_events':num_events}
    else:
        events = Events.objects.all().order_by('date') # order_by
        num_events = events.count() #count
        context = {'events': events, 'old_events': old_events, 'num_events':num_events}
    return render(request, 'EventsList.html', context)


def deleteEvent(request, event_id):
    event = Events.objects.get(pk=event_id)
    event.delete()
    return redirect('listEvents')  # Redirect to the event list page


 
