from django.contrib import admin
from .models import Author, Book, Teg
import random


def random_author(modeladmin, request, queryset):
    name = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina",
            "paul", "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal",
            "carl", "lady", "lauren", "ichabod", "arthur", "ashley", "drake",
            "kim", "julio", "lorraine", "floyd", "janet", "bill", "jill"]
    surname = ["barker", "style", "spirits", "murphy", "blacker", "bleacher",
               "rogers", "warren", "keller", "furry", "levi", "mash", "ost",
               "king", "speed", "star", "bird", "rain", "redneck", "trap"]

    name = random.choice(name).title()
    surname = random.choice(surname).title()
    patron = random.choice(name).title()
    email = name + surname + '@mail.com'
    phone = random.randint(10000000000, 99999999999)

    random_author = Author(name=name, surname=surname, patronymic=patron,
                           email=email.lower(), phone_number=phone)
    random_author.save()


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'display_book')
    actions = [random_author]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_teg')


class TegAdmin(admin.ModelAdmin):
    list_display = ('title', 'flag')
    list_filter = ('flag',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Teg, TegAdmin)
