from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializers import BooksSerializer
from book.models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
                       ]
    filterset_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['name', 'author_name', 'price']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


def auth(request):
    return render(request, 'oauth.html')
