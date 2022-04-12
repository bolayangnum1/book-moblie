from django.contrib import admin
from data.models import Book, Review, ReadingGoal, Author, AudioBook, ChoiceBook, ChoiceAudio


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'age_view']
    list_filter = ['name', 'language', 'age_view']
    search_fields = ['name', 'language', 'age_view']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'review', 'rating']
    list_filter = ['user', 'book', 'review', 'rating']
    search_fields = ['user', 'book', 'review', 'rating']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    list_filter = ['name', 'date']
    search_fields = ['name', 'date']


class AudioBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'age_view']
    list_filter = ['name', 'language', 'age_view']
    search_fields = ['name', 'language', 'age_view']


admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReadingGoal)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AudioBook, AudioBookAdmin)
admin.site.register(ChoiceBook)
admin.site.register(ChoiceAudio)
