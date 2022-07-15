from unittest import TestCase
from book.models import Book
from book.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='test book 1', price=25, author_name='author1')
        book_2 = Book.objects.create(name='test book 2', price=30, author_name='author2')
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'test book 1',
                'price': '25.00',
                'author_name': 'author1',
            },
            {
                'id': book_2.id,
                'name': 'test book 2',
                'price': '30.00',
                'author_name': 'author2',
            },
        ]
        self.assertEqual(expected_data, data)
