from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from book.views import BookViewSet, auth, UserBooksRelationView
from . import settings
from .yasg import urlpatterns as doc_urls
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'book_relation', UserBooksRelationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)
]
urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
