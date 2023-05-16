from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


# Create your views here.
@api_view(["GET"])
# 로그인한 사용자만 자기 정보를 볼 수 있도록
@permission_classes([IsAuthenticated])
def userinfo(request):
    # data= 일때는 내가 입력해서 수정한 정보
    # instance= 일 때는 새로운 데이터를 넣을 때
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data)