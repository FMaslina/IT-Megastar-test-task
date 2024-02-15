from django.core.management.base import BaseCommand
from django.core.management import call_command

from writers_and_books.models import WriterModel, BookModel


class Command(BaseCommand):
    help = 'Run server with initialization steps'

    def handle(self, *args, **options):
        # Выполняем создание миграций
        call_command('makemigrations', interactive=False)
        call_command('migrate', interactive=False)

        # Добавляем тестовые данные
        self.create_initial_data()

        # Запускаем сервер
        call_command('runserver', *args, **options)

    def create_initial_data(self):
        # Добавляем тестовых писателей
        self.create_writers()

        # Добавляем тестовые книги
        self.create_books()

    def create_writers(self):
        writers = [
            {'name': 'Александр Пушкин'},
            {'name': 'Лев Толстой'},
            {'name': 'Федор Достоевский'}
        ]
        for writer_data in writers:
            WriterModel.objects.create(**writer_data)

    def create_books(self):
        books = [
            {'title': 'Евгений Онегин', 'author_id': 1},
            {'title': 'Руслан и Людмила', 'author_id': 1},
            {'title': 'Капитанская дочка', 'author_id': 1},
            {'title': 'Война и мир', 'author_id': 2},
            {'title': 'Анна Каренина', 'author_id': 2},
            {'title': 'Воскресение', 'author_id': 2},
            {'title': 'Преступление и наказание', 'author_id': 3},
            {'title': 'Идиот', 'author_id': 3},
            {'title': 'Братья Карамазовы', 'author_id': 3},
        ]
        for book_data in books:
            BookModel.objects.create(**book_data)
