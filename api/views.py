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
    """
    List all user apps, or create a new app.
    """

    if request.method == "GET":
        apps = request.user.app_set
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
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

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def app_details(request, app_id):
    """
    Retrieve, update or delete a user app.
    """
    try:
        app = App.objects.get(pk=app_id)
    except App.DoesNotExist:
        return JsonResponse({
            'message': "Not found",
        }, status=404)
    
    if app.user != request.user:
        return JsonResponse({
            'message': "Not yours",
        }, status=403)

    if request.method == "GET":
        serializer = AppSerializer(app)
        return Response(serializer.data)
    
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AppSerializer(app, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse({
                'message': "Validation error",
                'errors': serializer.errors, 
            }, status=400)
        
    if request.method == "DELETE":
        app.delete()
        return JsonResponse({
            'message': "Successfully Deleted",
        }, status=200)
