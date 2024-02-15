from django.urls import path
from writers_and_books.views import GetAuthorAndBooksView

urlpatterns = [
    path('writers/<int:pk>/', GetAuthorAndBooksView.as_view(), name='get_author_and_books_view'),
]