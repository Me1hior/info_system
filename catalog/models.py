from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Verification(models.Model):
    created_by = models.ForeignKey(
        User,
        related_name='%(app_label)s_%(class)s_created_related',
        verbose_name=u'Создал',
        on_delete=models.SET_NULL,
        blank=True, null=True, )

    changed_by = models.ForeignKey(
        User,
        related_name='%(app_label)s_%(class)s_changed_related',
        verbose_name=u'Изменил',
        on_delete=models.SET_NULL,
        blank=True, null=True, )

    class Meta:
        abstract = True


class Author(Verification):
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество',
                                  blank=True)
    email = models.EmailField(verbose_name='Почта', blank=True)
    phone_regex = RegexValidator(
        regex=r'(\+)?\d{1}[\s\(]?\d{3}[\s\)]?\d{3}[\s-]?\d{2}[\s-]?\d{2}',
        message="Нужно вводить телефонный номер в формате +9(999)999-99-99")
    phone_number = models.CharField(validators=[phone_regex], max_length=16,
                                    verbose_name='Телефон', blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname

    def display_book(self):
        return ', '.join([book.title for book in self.book_set.all()])

    display_book.short_description = 'Книги автора'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Teg(models.Model):
    CHOICES = (
        (True, "Активен"),
        (False, 'Не активен'))
    title = models.CharField(max_length=30, verbose_name='Название',
                             unique=True)
    flag = models.BooleanField(max_length=50, choices=CHOICES,
                               verbose_name='Активность')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Book(Verification):
    title = models.CharField(max_length=50, verbose_name='Название')
    date_field = models.DateField(auto_now=False, verbose_name='Дата публикации', )
    description = models.TextField(max_length=800, verbose_name='Краткое описание ')
    image_field = models.ImageField(upload_to='images', verbose_name='Изображение-превью', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    teg = models.ManyToManyField(Teg, verbose_name='Тэг', blank=True)

    def __str__(self):
        return self.title

    def display_teg(self):
        return ', '.join([teg.title for teg in self.teg.all()])

    display_teg.short_description = 'Тэги'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
