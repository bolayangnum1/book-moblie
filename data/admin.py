from django.contrib import admin
from data.models import Book, Review, ReadingGoal, Author, Audio, ChoiceBook, ChoiceAudio


admin.site.register(Book)
admin.site.register(Review)
admin.site.register(ReadingGoal)
admin.site.register(Author)
admin.site.register(Audio)
admin.site.register(ChoiceBook)
admin.site.register(ChoiceAudio)