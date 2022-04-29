from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from .models import Author, ReadBook, ReviewBook, ReviewAudio, ReviewVideo, Category, BookList, VideoBook, AudioBook
from .permissions import IsOwnerOrReadOnly
from .serializers import AuthorSerializer, ReadBookSerializer, ReviewAudioSerializer, ReviewBookSerializer, ReviewVideoSerializer, AudioBookSerializer, VideoBookSerializer, BookListSerializer, CategorySerializer


class AuthBookViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all();
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filter_fields = ['name']


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = ReadBookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ReadBook.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'author', 'language', 'age_view']
    filter_fields = ['name', 'author', 'language', 'age_view']


class ReviewAudioViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewAudioSerializer
    queryset = ReviewAudio.objects.all()


class ReviewBookViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewBookSerializer
    queryset = ReviewBook.objects.all()


class ReviewVideoViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewVideoSerializer
    queryset = ReviewVideo.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BookListViewSet(viewsets.ModelViewSet):
    serializer_class = BookListSerializer
    queryset = BookList.objects.all()


class AudioBookViewSet(viewsets.ModelViewSet):
    serializer_class = AudioBookSerializer
    queryset = AudioBook.objects.all()


class VideoBookViewSet(viewsets.ModelViewSet):
    serializer_class = VideoBookSerializer
    queryset = VideoBook.objects.all()
