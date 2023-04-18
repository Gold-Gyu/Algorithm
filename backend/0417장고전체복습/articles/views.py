from django.shortcuts import render, get_object_or_404, get_list_or_404

# 데이터만 가져다 줄
from rest_framework.decorators import api_view
# 응답 객체를 만들어다줄
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# Create your views here.


# GET으로 조회 및 생성하기
@api_view(['GET', 'POST'])
def article_list(request):

    # GET이 들어오면 조회하기
    if request.method == 'GET':
        articles = Article.objects.all()
        # json형식으로 바꿔주기 위해 직렬화가 필요
        # serializer.py로 가서 작성
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    # POST로 들어오면 생성하기
    elif request.method == "POST":
        # 역직렬화 json을 파이썬으로
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 데이터가 유효하지 않은 데이터로 생성하려할 때 서버잘못이 아니고 클라이언트 잘못임을 알려주는 옵션, 유효하지 않아서 발생하는 에러는 400응답임을 반환한다.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 상세 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)


    # 데이터 상세 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 데이터 삭제하기
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 데이터 수정요청
    elif request.method == "PUT":
        # 다시 역직렬화
        serializer = ArticleSerializer(article, data=request.data) # article을 request.data로 변경
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
# 댓글을 가져다와서 직렬화하기
@api_view(['GET'])
def comment_list(request):

    # 잘 모르겠음 이부분
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# 댓글 상세조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
# 특정 게시글에 작성된 댓글 목록 출력하기
@api_view(['GET', "POST"])
def article_comments(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    # 특정 게시글에 작성된 댓글 출력 
    if request.method == "GET":
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    # 댓글 생성
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
