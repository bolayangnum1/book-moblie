from rest_framework import serializers
from .models import Author, Book, Review, ReadingGoal, PhotoUser, AudioBook


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'id', 'img', 'date']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['name', 'id', 'author', 'reader', 'img', 'text', 'copyright_holder', 'book', 'language', 'rating', 'tags']


class AudioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioBook
        fields = ['__all__']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['user', 'id', 'book', 'review', 'created_date', 'rating']


class ReadingGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingGoal
        fields = ['user', 'id', 'goal', 'time_period']


class PhotoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoUser
        fields = ['user', 'id', 'img']