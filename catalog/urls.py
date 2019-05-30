from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', base, name='base'),
    url(r'^author/list/$', AuthorListView.as_view(), name='author-list'),
    url(r'^author/create/', AuthorCreateView.as_view(), name='author-create'),
    url(r'^author/(?P<pk>\d+)/update/', AuthorUpdateView.as_view(), name='author-update'),
    url(r'^author/(?P<pk>\d+)/delete/', AuthorDeleteView.as_view(), name='author-delete', ),
    url(r'^book/create/', BookCreateView.as_view(), name='book-create'),
    url(r'^book/(?P<pk>\d+)/update/', BookUpdateView.as_view(), name='book-update'),
    url(r'^book/(?P<pk>\d+)/delete/', BookDeleteView.as_view(), name='book-delete'),
    url(r'^book/(?P<search>.+)/', BookListView.as_view(), name='book-list'),
    url(r'^teg/list/', TegListView.as_view(), {'fltr': 'all'}, name='teg-list'),
    url(r'^teg/active/', TegListView.as_view(), {'fltr': 'active'}, name='teg-list-active'),
    url(r'^teg/nonactive/', TegListView.as_view(), {'fltr': 'nonactive'}, name='teg-list-nonactive'),
    url(r'^teg/create/', TegCreateView.as_view(), name='teg-create'),
    url(r'^teg/(\d{1,2})/update/', TegUpdateView.as_view(), name='teg-update'),
    url(r'^teg/(\d{1,2})/delete/', TegDeleteView.as_view(), name='teg-delete'), ]
