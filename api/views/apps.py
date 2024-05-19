from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from vault.serializers import AppSerializer
from vault.models import App
from api.forms import AppForm

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list(request):
    """
    List all user apps, or create a new app.
    """

    if request.method == "GET":
        apps = request.user.app_set
        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()

            serializer = AppSerializer(app)
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse({
                'message': "validation error",
                'errors': serializer.errors, 
            }, status=400)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def details(request, id):
    """
    Retrieve or update a user app.
    """
    try:
        app = App.objects.get(pk=id)
    except App.DoesNotExist:
        return JsonResponse({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return JsonResponse({
            'message': "invalid UUID",
        }, status=400)
    
    if app.user != request.user:
        return JsonResponse({
            'message': "Not yours",
        }, status=403)

    if request.method == "GET":
        serializer = AppSerializer(app)
        return Response(serializer.data)
    
    if request.method == "POST":
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()

            serializer = AppSerializer(app)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    """
    Delete a user app.
    """
    try:
        app = App.objects.get(pk=id)
    except App.DoesNotExist:
        return JsonResponse({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return JsonResponse({
            'message': "invalid UUID",
        }, status=400)
    
    if app.user != request.user:
        return JsonResponse({
            'message': "Not yours",
        }, status=403)
   
    if request.method == "POST":
        app.delete()
        return JsonResponse({
            'message': "Successfully Deleted",
        }, status=200)