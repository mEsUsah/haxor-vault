import datetime
from django.db import IntegrityError
from django.db.models import Max
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from api.serializers import AppSerializer
from vault.models import App

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def app_list(request):
    if request.method == "GET":
        apps = request.user.app_set
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = request.user.id

        serializer = AppSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse({
                'message': "validation error",
                'errors': serializer.errors, 
            }, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def app_details(request, app_id):
    pass