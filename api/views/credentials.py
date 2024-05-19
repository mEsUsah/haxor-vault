from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from vault.serializers import CredentialSerializer
from vault.models import Credential
from vault.forms import CredentialForm

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list(request):
    """
    List all credentials, or create a new credential.
    Will not allow user to create a credential for an app that is not theirs.
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
                return Response({
                    'message': "Not your app",
                }, status=403)
            credential.save()

            serializer = CredentialSerializer(credential)
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
    View or update a credential.
    Will not allow user to view or update a credential for an app that is not theirs.
    """

    try:
        credential = Credential.objects.get(pk=id)
    except Credential.DoesNotExist:
        return Response({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return Response({
            'message': "invalid UUID",
        }, status=400)
    
    if credential.app.user != request.user:
        return Response({
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
                return Response({
                    'message': "Not your app",
                }, status=403)
            credential.save()

            serializer = CredentialSerializer(credential)
            return Response(serializer.data, status=200)
        else:
            return Response({
                'message': "Validation error",
                'errors': form.errors, 
            }, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    """
    Retrieve, update or delete a user credential.
    Will not allow user to delete a credential for an app that is not theirs.
    """

    try:
        credential = Credential.objects.get(pk=id)
    except Credential.DoesNotExist:
        return Response({
            'message': "Not found",
        }, status=404)
    except ValidationError:
        return Response({
            'message': "invalid UUID",
        }, status=400)
    
    if credential.app.user != request.user:
        return Response({
            'message': "Not yours",
        }, status=403)

    
    if request.method == "POST":
        credential.delete()
        return Response({
            'message': "Successfully deleted credential",
        }, status=200)