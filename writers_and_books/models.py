from django.db import models


class WriterModel(models.Model):
    name = models.TextField(verbose_name="Имя")

    class Meta:
        verbose_name = "Писатель"
        verbose_name_plural = "Писатели"


class BookModel(models.Model):
    author = models.ForeignKey(WriterModel, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.TextField(verbose_name="Название")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
