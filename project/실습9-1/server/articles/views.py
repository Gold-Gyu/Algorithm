
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer
from .models import Article

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        print(request.user)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)