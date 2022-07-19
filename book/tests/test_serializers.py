# from unittest import TestCase
#
# from django.contrib.auth.models import User
#
# from book.models import Book
# from book.serializers import BooksSerializer
#
#
# class BookSerializerTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='test_username')
#         self.book_1 = Book.objects.create(name='test book 1', price=25, author_name='author1', owner='User')
#         self.book_2 = Book.objects.create(name='test book 2', price=30, author_name='author2', owner='User')
#
#     def test_ok(self):
#         data = BooksSerializer([self.book_1, self.book_2], many=True).data
#         expected_data = [
#             {
#                 'id': self.book_1.id,
#                 'name': 'test book 1',
#                 'price': '25.00',
#                 'author_name': 'author1',
#             },
#             {
#                 'id': self.book_2.id,
#                 'name': 'test book 2',
#                 'price': '30.00',
#                 'author_name': 'author2',
#             },
#         ]
#         self.assertEqual(expected_data, data)
