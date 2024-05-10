import datetime
from django.db import IntegrityError
from django.db.models import Max
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def app_index(request):
    pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def app(request, app_id):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def app_create(request, app_id):
    pass