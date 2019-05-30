from rest_framework import serializers
from .models import Author, Book, Teg


class AuthorDetailSerializers(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    changed_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = '__all__'


class AuthorListSerializers(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    changed_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = '__all__'


class BookDetailSerializers(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    changed_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class TegDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = '__all__'


class TegListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = '__all__'


class TegUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
