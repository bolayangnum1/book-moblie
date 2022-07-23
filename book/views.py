from django.db.models import Count, Case, When, Avg
from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import BooksSerializer, UserBookRelationSerializer
from book.models import Book, UserBookRelation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')
            ).select_related('owner').prefetch_related('readers').order_by('id')
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


class UserBooksRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = 'book'

    def get_object(self):
        obj, _ = UserBookRelation.objects.get_or_create(user=self.request.user,
                                                        book_id=self.kwargs['book'])
        return obj


def auth(request):
    return render(request, 'oauth.html')
