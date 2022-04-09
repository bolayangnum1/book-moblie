from django.contrib import admin
from data.models import Book, Review, ReadingGoal


admin.site.register(Book)
admin.site.register(Review)
admin.site.register(ReadingGoal)