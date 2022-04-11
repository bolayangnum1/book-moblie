from rest_framework import serializers
from .models import Author, Book, Review, ReadingGoal, PhotoUser


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'id', 'img', 'date']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['name', 'id', 'author', 'reader', 'img', 'text', 'copyright_holder', 'book', 'price', 'language', 'rating', 'tags']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['user', 'id', 'book', 'review', 'created_date', 'rating']


class ReadingGoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingGoal
        fields = ['user', 'id', 'book', 'time_period']


class PhotoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoUser
        fields = ['user', 'id', 'img']