import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from book.models import Book, UserBookRelation
from book.serializers import BooksSerializer


class BookApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')

        self.book_1 = Book.objects.create(name='Test book 1', price=25,
                                          author_name='Author 1', owner=self.user)
        self.book_2 = Book.objects.create(name='Test book 2', price=55,
                                          author_name='Author 5', owner=self.user)
        self.book_3 = Book.objects.create(name='Test book Author 1', price=55,
                                          author_name='Author 2', owner=self.user)

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'price': 55})
        serializer_data = BooksSerializer([self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BooksSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Book.objects.all().count())
        url = reverse('book-list')
        data = {
            'name': 'test book 1',
            'price': 25,
            'author_name': 'author1',
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Book.objects.all().count())
        self.assertEqual(self.user, Book.objects.last().owner)

    def test_update(self):
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            'name': self.book_1.name,
            'price': 100,
            'author_name': self.book_1.author_name,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(100, self.book_1.price)

    def test_delete(self):
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            'name': self.book_1.name,
            'price': 100,
            'author_name': self.book_1.author_name,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.delete(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, Book.objects.all().count())

    def test_update_not_owner(self):
        self.user_2 = User.objects.create(username='test_username_2',)
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            'name': self.book_1.name,
            'price': 100,
            'author_name': self.book_1.author_name,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user_2)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(25, self.book_1.price)
        self.assertEqual({'detail': ErrorDetail(string='У вас недостаточно прав для выполнения данного действия.', code='permission_denied')}, response.data)

    def test_delete_not_owner(self):
        self.user_2 = User.objects.create(username='test_username_2',)
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            'name': self.book_1.name,
            'price': 100,
            'author_name': self.book_1.author_name,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.delete(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, Book.objects.all().count())
        self.assertEqual(25, self.book_1.price)
        self.assertEqual(None, response.data)

    def test_update_not_owner_but_staff(self):
        self.user_2 = User.objects.create(username='test_username_2', is_staff=True)
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            'name': self.book_1.name,
            'price': 100,
            'author_name': self.book_1.author_name,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user_2)
        response = self.client.put(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(100, self.book_1.price)


class BookRelationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.user_2 = User.objects.create(username='test_username_2')

        self.book_1 = Book.objects.create(name='Test book 1', price=25,
                                          author_name='Author 1', owner=self.user)
        self.book_2 = Book.objects.create(name='Test book 2', price=55,
                                          author_name='Author 5', owner=self.user)

    def test_like(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))
        data = {
            'like': True,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.like)
        data = {
            'in_bookmarks': True,
        }

        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.in_bookmarks)

    def test_rate(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))
        data = {
            'rate': 5,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertEqual(5, relation.rate)

    def test_rate_wrong(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))
        data = {
            'rate': 2,
        }

        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code, response.data)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertEqual(2, relation.rate)


