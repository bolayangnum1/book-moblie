from .models import Book, UserBookRelation
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')


@admin.register(UserBookRelation)
class UserBookRelationAdmin(admin.ModelAdmin):
    pass
