from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework import status
from .models import Calendar, Event, Notification
from .serializers import CalendarSerializer, EventSerializer, UserSerializer, NotificationSerializer
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404


#Calendar apis ============================================================

@api_view(['GET'])
def getCalendar(request):
    calendars = Calendar.objects.all()
    serializer = CalendarSerializer(calendars, many =True)
    return Response(serializer.data) 

@api_view(['POST'])
def addCalendar(request):
    serializer = CalendarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCalendar(request, calendar_id):
    try:
        calendar = Calendar.objects.get(pk=calendar_id)
    except Calendar.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    calendar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def updateCalendar(request, calendar_id):
    try:
        calendar = Calendar.objects.get(pk=calendar_id)
    except Calendar.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    # Determine the HTTP method based on the request data
    if 'name' in request.data and 'description' in request.data:
        # If both 'name' and 'description' fields are provided, perform a PUT operation.
        serializer = CalendarSerializer(calendar, data=request.data)
    else:
        # If any field is missing, perform a PATCH operation.
        serializer = CalendarSerializer(calendar, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Event api points ===============================================================

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getEvent(request, calendar_key):
    events = Event.objects.filter(calendar_key = calendar_key)
    serializer = EventSerializer(events, many =True)
    return Response(serializer.data) 

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addEvent(request, calendar_key):

    # Select the Calendar object based on the calendar_key from the URL
    try:
        calendar = Calendar.objects.get(id=calendar_key)
    except Calendar.DoesNotExist:
        return Response({"detail": "Calendar not found."}, status=status.HTTP_404_NOT_FOUND)

    # Set the calendar field of the event to the retrieved calendar
    request.data['calendar_key'] = calendar.id

    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteEvent(request, event_id, calendar_key):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateEvent(request, event_id, calendar_key):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    # Determine the HTTP method based on the request data
    serializer = EventSerializer(event, data=request.data, partial=True)


    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Autentications api points ======================================================

@api_view(['POST'])
def signin(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."})
    
    # Get or create a token for the user
    token, created = Token.objects.get_or_create(user=user)
    
    # Note the correction here: "instance" instead of "istance"
    serializer = UserSerializer(instance=user)
    
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_token(request):
    # If the code reaches here, it means the token is valid
    return Response({'message': 'Token is valid'})

#Notification api points ======================================================

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getNotification(request):

    user = request.user
    notifications = Notification.objects.filter(user_key=user)
    serializer = NotificationSerializer(notifications, many =True)
    return Response(serializer.data) 
