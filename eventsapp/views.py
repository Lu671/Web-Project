from django.shortcuts import render, redirect
from .models import Events
from .forms import EventForm
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    events = Events.objects.all().values('date', 'title')
    events_list = [{'date': event['date'].strftime('%Y-%m-%d'), 'title': event['title']} for event in events]
    context = {
        'events_list_json': json.dumps(events_list)
    }
    return render(request, 'home.html', context)


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
# Add count and order by (( add the register to attend events in lpther model.))
def listEvents(request):
    month_names = {1: 'January',2: 'February',3: 'March',4: 'April',5: 'May',
                   6: 'June',7: 'July',8: 'August',9: 'September',10: 'October',
                   11: 'November',12: 'December'}
    hardcoded_events = [
    {'title': 'Event 1', 'date': '2024-03-15', 'description': 'Tech workshop', 'location':'Computer College','agenda':'media\Event 1 Agenda.pdf'},
    {'title': 'Event 2', 'date': '2024-04-15', 'description': 'Programming Competition','location':'Computer College','agenda':'media\Event 2 Agenda.pdf'},
    ]
    selected_month = request.GET.get('month')
    month_name = month_names.get(int(selected_month)) if selected_month else None
    if selected_month:
        events = Events.objects.filter(date__month=selected_month).order_by('date')
        num_events = events.count()
        context = {'events': events, 'month':month_name, 'hardcoded_events': hardcoded_events, 'num_events':num_events}
    else:
        events = Events.objects.all().order_by('date')
        num_events = events.count()
        context = {'events': events, 'hardcoded_events': hardcoded_events, 'num_events':num_events}
    return render(request, 'EventsList.html', context)
   

def deleteEvent(request, event_id):
    event = Events.objects.get(pk=event_id)
    event.delete()
    return redirect('listEvents')  # Redirect to the event list page
 

 # Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')
     
    # Render the login page template (GET request)
    return render(request, 'login.html')
 
# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/register/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
     
    # Render the registration page template (GET request)
    return render(request, 'register.html')

@login_required
def register_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    request.user.registered_events.add(event)
    return redirect('listEvents')

@login_required
def registered_events(request):
    events = request.user.registered_events.all()
    return render(request, 'registered_events.html', {'events': events})