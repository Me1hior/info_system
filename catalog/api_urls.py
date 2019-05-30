from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^author/create/', AuthorCreateAPIView.as_view(), name='author-create-api'),
    url(r'^author/list/', AuthorListAPIView.as_view(), name='author-list-api'),
    url(r'^author/detail/(?P<pk>[0-9]+)/', AuthorDetailAPIView.as_view(), name='author-detail-api'),
    url(r'^book/create/', BookCreateAPIView.as_view(), name='book-create-api'),
    url(r'^book/list/', BookListAPIView.as_view(), name='book-list-api'),
    url(r'^book/detail/(?P<pk>[0-9]+)/', BookDetailAPIView.as_view(), name='book-detail-api'),
    url(r'^teg/create/', TegCreateAPIView.as_view(), name='teg-create-api'),
    url(r'^teg/list/', TegListAPIView.as_view(), name='teg-list-api'),
    url(r'^teg/detail/(?P<pk>[0-9]+)/', TegDetailAPIView.as_view(), name='teg-detail-api'),
    url(r'^teg/update/(?P<pk>[0-9]+)/', TegUpdateView.as_view(), name='teg-update-api'), ]
