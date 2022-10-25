from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import *
from post.serializers import *
from rest_framework import status

# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        # try except error handling
        try:
            article = Article.objects.all()
            serializer = ArticleSerializer(article, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'something went wrong in articles'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


class ArticleSingleView(APIView):
    def get(self, request, id):
        try:
            article = Article.objects.get(id=id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'something went wrong in articles'}, status=status.HTTP_400_BAD_REQUEST)


class ReviewView(APIView):
    def get(self, request):
        try:
            review = Review.objects.all()
            serializer = ReviewSerializer(review, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'something went wrong in reviews'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        

class ReviewSingleView(APIView):
    def get(self, request, id):
        try:
            review = Review.objects.get(id=id)
            serializer = ReviewSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'something went wrong in reviews'}, status=status.HTTP_400_BAD_REQUEST)
