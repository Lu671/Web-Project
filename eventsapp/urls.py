from django.urls import path,include
from eventsapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('addEvent',views.addEvent,name='addEvent'),
    path('eventsList',views.listEvents,name='listEvents'),
    path('event/delete/<int:event_id>/', views.deleteEvent, name='delete_event'),
     path('login/', views.login_page, name='login'),    # Login page
    path('register/', views.register_page, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('events/<int:event_id>/register/', views.register_event, name='register_event'),
    path('registered_events/events', views.registered_events, name='registered_events'),
]
