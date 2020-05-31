from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from cornerapps.user.serializers import AuthLoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authLogin(request):
    serializer = AuthLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, token = serializer.save()
    return Response({
        'token': token,
        'user': user,
    })
