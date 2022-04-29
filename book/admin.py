from django.contrib import admin
from book.models import ReadBook, AudioBook, VideoBook, Author, Category, BookList, ReviewBook, ReviewAudio, ReviewVideo


class ReviewBookinline(admin.TabularInline):
    model = ReviewBook
    extra = 0


class ReviewVideoinline(admin.TabularInline):
    model = ReviewVideo
    extra = 0


class ReviewAudioinline(admin.TabularInline):
    model = ReviewAudio
    extra = 0


class AudioBookAdmin(admin.ModelAdmin):
    inlines = [ReviewAudioinline]


class ReadBookAdmin(admin.ModelAdmin):
    inlines = [ReviewBookinline]


class VideoBookAdmin(admin.ModelAdmin):
    inlines = [ReviewVideoinline]


admin.site.register(ReadBook, ReadBookAdmin)
admin.site.register(AudioBook, AudioBookAdmin)
admin.site.register(VideoBook, VideoBookAdmin)
admin.site.register(BookList)
admin.site.register(Author)
admin.site.register(Category)

