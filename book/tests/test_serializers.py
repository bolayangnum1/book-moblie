from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models import Count, When, Case, Avg
from book.models import Book, UserBookRelation
from book.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        test_user_1 = User.objects.create(username='test_user_1',
                                          first_name='Bolot', last_name='Adanov')
        test_user_2 = User.objects.create(username='test_user_2',
                                          first_name='Adanov', last_name='Bolot')
        test_user_3 = User.objects.create(username='test_user_3',
                                          first_name='1', last_name='2')

        book_1 = Book.objects.create(name='test book 1', price=25, author_name='author1', owner=test_user_1)
        book_2 = Book.objects.create(name='test book 2', price=30, author_name='author2')

        UserBookRelation.objects.create(user=test_user_1, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=test_user_2, book=book_1, like=True, rate=4)
        UserBookRelation.objects.create(user=test_user_3, book=book_1, like=True, rate=3)

        UserBookRelation.objects.create(user=test_user_1, book=book_2, like=True, rate=5)
        UserBookRelation.objects.create(user=test_user_2, book=book_2, like=False, rate=3)
        UserBookRelation.objects.create(user=test_user_3, book=book_2, like=False)

        books = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')).order_by('id')
        data = BooksSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'test book 1',
                'price': '25.00',
                'author_name': 'author1',
                'likes_count': 3,
                'annotated_likes': 3,
                'rating': '4.00',
                'owner_name': 'test_user_1',
                'readers': [
                    {
                        'first_name': 'Bolot',
                        'last_name': 'Adanov',
                    },
                    {
                        'first_name': 'Adanov',
                        'last_name': 'Bolot',
                    },
                    {
                        'first_name': '1',
                        'last_name': '2',
                    },

                ]

            },
            {
                'id': book_2.id,
                'name': 'test book 2',
                'price': '30.00',
                'author_name': 'author2',
                'likes_count': 1,
                'annotated_likes': 1,
                'rating': '4.00',
                'owner_name': '',
                'readers': [
                    {
                        'first_name': 'Bolot',
                        'last_name': 'Adanov',
                    },
                    {
                        'first_name': 'Adanov',
                        'last_name': 'Bolot',
                    },
                    {
                        'first_name': '1',
                        'last_name': '2',
                    },

                ]
            },
        ]
        self.assertEqual(expected_data, data, print(expected_data, f'\n{data}'))

