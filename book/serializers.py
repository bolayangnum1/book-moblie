from rest_framework import serializers
from .models import Author, ReadBook, ReviewBook, ReviewAudio, ReviewVideo, AudioBook, VideoBook, BookList, Category


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'id', 'img', 'date', 'date_dead']


class ReviewVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewVideo
        fields = '__all__'

    def get_likes_count(self, instance):
        return ReviewVideo.objects.filter(book=instance, like=True).count()


class ReviewBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewBook
        fields = '__all__'

    def get_likes_count(self, instance):
        return ReviewBook.objects.filter(book=instance, like=True).count()


class ReviewAudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewAudio
        fields = '__all__'

    def get_likes_count(self, instance):
        return ReviewAudio.objects.filter(book=instance, like=True).count()


class ReadBookSerializer(serializers.ModelSerializer):
    review_book_detail = ReviewBookSerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = ReadBook
        fields = ('id', 'owner', 'author', 'name', 'img', 'text', 'copyright_holder', 'book', 'rating', 'language', 'year_book', 'age_view', 'book_type', 'book_list',
                  'review_book_detail', 'author')


class AudioBookSerializer(serializers.ModelSerializer):
    review_audio_detail = ReviewAudioSerializer(many=True)
    author = AuthorSerializer(many=True)

    class Meta:
        model = AudioBook
        fields = ('id', 'owner', 'author', 'name', 'img', 'text', 'copyright_holder', 'audio', 'rating', 'language', 'year_book', 'age_view', 'book_type', 'book_list',
                  'review_audio_detail', 'author')


class VideoBookSerializer(serializers.ModelSerializer):
    review_video_detail = ReviewVideoSerializer(many=True)
    author = AuthorSerializer(many=True)

    class Meta:
        model = VideoBook
        fields = ('id', 'owner', 'author', 'name', 'video', 'rating', 'book_type', 'booklist',
                  'review_video_detail', 'author')


class BookListSerializer(serializers.ModelSerializer):
    read_book_detail = ReadBookSerializer(many=True)
    book_list_detail = ReadBookSerializer(many=True)
    book_video_detail = ReadBookSerializer(many=True)

    class Meta:
        model = BookList
        fields = ('id', 'name', 'category', 'read_book_detail', 'book_list_detail', 'book_video_detail')


class CategorySerializer(serializers.ModelSerializer):
    category_detail = BookListSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name_category', 'id', 'img', 'category_detail')
