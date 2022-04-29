from django.urls import path
from .views import AuthBookViewSet, BookViewSet, ReviewAudioViewSet, ReviewVideoViewSet, ReviewBookViewSet, VideoBookViewSet, AudioBookViewSet, CategoryViewSet, BookListViewSet


urlpatterns = [
    path('category-list/', CategoryViewSet.as_view({'get': 'list'})),
    path('category-detail/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),

    path('book-list-list/', BookListViewSet.as_view({'get': 'list'})),
    path('book-list-detail/<int:pk>/', BookListViewSet.as_view({'get': 'retrieve'})),

    path('video-book-list/', VideoBookViewSet.as_view({'get': 'list'})),
    path('video-book-detail/<int:pk>/', VideoBookViewSet.as_view({'get': 'retrieve'})),
    path('video-book-delete/<int:pk>/', VideoBookViewSet.as_view({'delete': 'destroy'})),

    path('audio-book-list/', AudioBookViewSet.as_view({'get': 'list'})),
    path('audio-book-detail/<int:pk>/', AudioBookViewSet.as_view({'get': 'retrieve'})),
    path('audio-book-delete/<int:pk>/', AudioBookViewSet.as_view({'delete': 'destroy'})),

    path('video-book-list/', VideoBookViewSet.as_view({'get': 'list'})),
    path('video-book-detail/<int:pk>/', VideoBookViewSet.as_view({'get': 'retrieve'})),
    path('video-book-list/<int:pk>/', VideoBookViewSet.as_view({'delete': 'destroy'})),

    path('book-review-create/', ReviewBookViewSet.as_view({'post': 'create'})),
    path('book-review-list/', ReviewBookViewSet.as_view({'get': 'list'})),
    path('book-review-delete/<int:pk/', ReviewBookViewSet.as_view({'delete': 'destroy'})),
    path('book-review-detail/<int:pk>/', ReviewBookViewSet.as_view({'get': 'retrieve'})),

    path('video-review-create/', ReviewVideoViewSet.as_view({'post': 'create'})),
    path('video-review-list/', ReviewVideoViewSet.as_view({'get': 'list'})),
    path('video-review-delete/<int:pk/', ReviewVideoViewSet.as_view({'delete': 'destroy'})),
    path('video-review-detail/<int:pk>/', ReviewVideoViewSet.as_view({'get': 'retrieve'})),

    path('audio-review-create/', ReviewAudioViewSet.as_view({'post': 'create'})),
    path('audio-review-list/', ReviewAudioViewSet.as_view({'get': 'list'})),
    path('audio-review-delete/<int:pk/', ReviewAudioViewSet.as_view({'delete': 'destroy'})),
    path('audio-review-detail/<int:pk>/', ReviewAudioViewSet.as_view({'get': 'retrieve'})),

    path('author-book-list/', AuthBookViewSet.as_view({'get': 'list'})),
    path('author-book-detail/<int:pk>/', AuthBookViewSet.as_view({'get': 'retrieve'})),

    path('read-book-list/', BookViewSet.as_view({'get': 'list'})),
    path('read-book-delete/<int:pk>/', BookViewSet.as_view({'delete': 'destroy'})),
    path('read-book-detail/<int:pk>/', BookViewSet.as_view({'get': 'retrieve'})),
]