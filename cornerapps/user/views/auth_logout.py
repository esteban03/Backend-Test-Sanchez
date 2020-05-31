from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated, ])
def authLogout(request):
    request.user.auth_token.delete()
    return Response({
        'status': 'success'
    })
