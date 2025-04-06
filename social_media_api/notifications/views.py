from django.shortcuts import render
from .models import Notification
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)