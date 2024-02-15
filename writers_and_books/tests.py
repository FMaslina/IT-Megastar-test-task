from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from writers_and_books.models import WriterModel, BookModel


class GetAuthorAndBooksTestCase(APITestCase):
    def test_get(self):
        writer = WriterModel.objects.create(name='test')
        BookModel.objects.create(title='test', author=writer)
        url = reverse('get_author_and_books_view', args=[1])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        data = {
            "id": 1,
            "name": "test",
            "books": [
                {
                    "id": 1,
                    "title": "test"
                }
            ]
        }
        
        self.assertEqual(data, response.data)
