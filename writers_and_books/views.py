from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from writers_and_books.misc import get_writer_and_books


class GetAuthorAndBooksView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']

        try:
            data = get_writer_and_books(pk)
            return Response(data=data, status=status.HTTP_200_OK)
        except BaseException:
            return Response(status=status.HTTP_404_NOT_FOUND)
