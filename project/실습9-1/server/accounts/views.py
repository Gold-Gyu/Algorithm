from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

@api_view(["GET:"])
@permission_classes([IsAuthenticated])
def userinfo(request):
  serializer = UserSerializer(request.user)
  return Response(serializer.data)
# Create your views here.
