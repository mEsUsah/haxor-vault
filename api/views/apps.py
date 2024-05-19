from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from vault.serializers import AppSerializer
from vault.models import App
from vault.forms import AppForm

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list(request):
    """
    View all apps, or create a new app.
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
            return Response(serializer.data, status=201)
        else:
            return Response({
                'message': "validation error",
                'errors': serializer.errors, 
            }, status=400)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def details(request, id):
    """
    View or update app.
    """

    try:
        app = App.objects.get(pk=id)
    except App.DoesNotExist:
        return Response({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return Response({
            'message': "invalid UUID",
        }, status=400)
    
    if app.user != request.user:
        return Response({
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
            return Response(serializer.data, status=200)
        else:
            return Response({
                'message': "Validation error",
                'errors': serializer.errors, 
            }, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    """
    Delete app.
    """

    try:
        app = App.objects.get(pk=id)
    except App.DoesNotExist:
        return Response({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return Response({
            'message': "invalid UUID",
        }, status=400)
    
    if app.user != request.user:
        return Response({
            'message': "Not yours",
        }, status=403)
   
    if request.method == "POST":
        app.delete()
        return Response({
            'message': "Successfully deleted app",
        }, status=200)