from django.urls import path
from . import views

urlpatterns = [
    # Authentication api points
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('check-token/', views.check_token, name='check-token'),

    # Notification api points 
    path('notification/get/', views.getNotification, name='get_notification'),

    # Calendar api points
    path('', views.getCalendar, name='get-calendar'),
    path('add/', views.addCalendar, name='add-calendar'),
    path('delete/<str:calendar_id>/', views.deleteCalendar, name='delete-calendar'),
    path('update/<str:calendar_id>/', views.updateCalendar, name='update-calendar'),

    # Event api points
    path('<str:calendar_key>/', views.getEvent, name='get-event'),
    path('<str:calendar_key>/add/', views.addEvent, name='add-event'),
    path('<str:calendar_key>/delete/<str:event_id>/', views.deleteEvent, name='delete-event'),
    path('<str:calendar_key>/update/<str:event_id>/', views.updateEvent, name='update-event'),
]
