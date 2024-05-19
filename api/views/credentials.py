from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from vault.serializers import CredentialSerializer
from vault.models import Credential
from vault.forms import CredentialForm

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list(request):
    """
    List all user credentials, or create a new credential.
    """
    if request.method == "GET":
        credentials = Credential.objects.filter(app__user=request.user)
        serializer = CredentialSerializer(credentials, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        form = CredentialForm(request.POST)
        if form.is_valid():
            credential = form.save(commit=False)
            if credential.app.user != request.user:
                return JsonResponse({
                    'message': "Not your app",
                }, status=403)
            credential.save()

            serializer = CredentialSerializer(credential)
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
    Retrieve, update or delete a user credential.
    """
    try:
        credential = Credential.objects.get(pk=id)
    except Credential.DoesNotExist:
        return JsonResponse({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return JsonResponse({
            'message': "invalid UUID",
        }, status=400)
    
    if credential.app.user != request.user:
        return JsonResponse({
            'message': "Not yours",
        }, status=403)

    if request.method == "GET":
        serializer = CredentialSerializer(credential)
        return Response(serializer.data)
    
    if request.method == "POST":
        form = CredentialForm(request.POST,  instance=credential)
        if form.is_valid():
            credential = form.save(commit=False)
            if credential.app.user != request.user:
                return JsonResponse({
                    'message': "Not your app",
                }, status=403)
            credential.save()

            serializer = CredentialSerializer(credential)
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse({
                'message': "Validation error",
                'errors': form.errors, 
            }, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    """
    Retrieve, update or delete a user credential.
    """
    try:
        credential = Credential.objects.get(pk=id)
    except Credential.DoesNotExist:
        return JsonResponse({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return JsonResponse({
            'message': "invalid UUID",
        }, status=400)
    
    if credential.app.user != request.user:
        return JsonResponse({
            'message': "Not yours",
        }, status=403)

    
    if request.method == "POST":
        credential.delete()
        return JsonResponse({
            'message': "Successfully Deleted",
        }, status=200)