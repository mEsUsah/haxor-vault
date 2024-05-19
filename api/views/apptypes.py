from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from vault.models import AppType
from vault.serializers import AppTypeSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    """
    List all app types.
    """

    if request.method == "GET":
        appTypes = AppType.objects.all()
        serializer = AppTypeSerializer(appTypes, many=True)
        return Response(serializer.data)