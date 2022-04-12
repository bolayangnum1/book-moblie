from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Author, Book, Review, ReadingGoal
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer, ReadingGoalSerializer


class AuthBookViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all();
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filter_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'author', 'language', 'age_view']
    filter_fields = ['name', 'author', 'language', 'age_view']


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReadingGoalViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingGoalSerializer
    queryset = ReadingGoal.objects.all()
