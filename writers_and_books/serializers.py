from rest_framework import serializers
from writers_and_books.models import WriterModel, BookModel


class WriterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterModel
        fields = "__all__"


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"
