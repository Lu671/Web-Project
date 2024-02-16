from django.urls import path,include
from eventsapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('/addEvent',views.addEvent,name='addEvent'),
    path('/eventsList',views.listEvents,name='listEvents')
]
