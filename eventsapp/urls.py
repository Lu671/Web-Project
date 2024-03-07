from django.urls import path,include
from eventsapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addEvent',views.addEvent,name='addEvent'),
    path('eventsList',views.listEvents,name='listEvents')
]
