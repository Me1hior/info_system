from django.forms import *
from .models import Author, Teg, Book


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class TegForm(ModelForm):
    class Meta:
        model = Teg
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        filter = '__all__'
        fields = ['title', 'date_field', 'description', 'image_field',
                  'author', 'teg', ]
