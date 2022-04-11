from rest_framework import generics, viewsets
from .models import Author, Book, Review, ReadingGoal
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer, ReadingGoalSerializer


class AuthBookViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all();
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReadingGoalViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingGoalSerializer
    queryset = ReadingGoal.objects.all()
