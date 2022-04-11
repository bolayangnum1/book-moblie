from django.urls import path
from .views import AuthBookViewSet, BookViewSet, ReviewViewSet, ReadingGoalViewSet


urlpatterns = [
    path('reading-goal/', ReadingGoalViewSet.as_view({'post': 'create'})),
    path('reading-goal/', ReadingGoalViewSet.as_view({'get': 'list'})),
    path('reading-goal/<int:pk>/', ReadingGoalViewSet.as_view({'patch': 'update'})),
    path('reading-goal/<int:pk>/', ReadingGoalViewSet.as_view({'delete': 'destroy'})),
    path('reading-goal/<int:pk>/', ReadingGoalViewSet.as_view({'get': 'retrieve'})),

    path('review-create/', ReviewViewSet.as_view({'post': 'create'})),
    path('review-list/', ReviewViewSet.as_view({'get': 'list'})),
    path('review-update/<int:pk>/', ReviewViewSet.as_view({'patch': 'update'})),
    path('review-delete/<int:pk/', ReviewViewSet.as_view({'delete': 'destroy'})),
    path('review-create/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'})),

    path('author-book-create/', AuthBookViewSet.as_view({'post': 'create'})),
    path('author-book-list/', AuthBookViewSet.as_view({'get': 'list'})),
    path('author-book-update/<int:pk>/', AuthBookViewSet.as_view({'patch': 'update'})),
    path('author-book-delete/<int:pk>/', AuthBookViewSet.as_view({'delete': 'destroy'})),
    path('author-book-detail/<int:pk>/', AuthBookViewSet.as_view({'get': 'retrieve'})),

    path('book-create/', BookViewSet.as_view({'post': 'create'})),
    path('book-list/', BookViewSet.as_view({'get': 'list'})),
    path('book-update/<int:pk>/', BookViewSet.as_view({'patch': 'update'})),
    path('book-delete/<int:pk>/', BookViewSet.as_view({'delete': 'destroy'})),
    path('book-detail/<int:pk>/', BookViewSet.as_view({'get': 'retrieve'})),
]