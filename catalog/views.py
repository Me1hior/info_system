from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from .serializers import *
from rest_framework import generics
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def base(request):
    return render(request, 'base.html', {})


class AuthorListView(ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'authors'

    def get(self, request):
        if 'search' in request.GET:
            query = request.GET['search']
            self.object_list = self.model.objects.filter(
                Q(name=query) | Q(email=query))
        else:
            self.object_list = self.get_queryset()
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def get_queryset(self):
        articles = self.model.objects.all()
        paginator = Paginator(articles, 6)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        return articles


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'catalog/author_create.html'
    form_class = forms.AuthorForm

    def post(self, request):
        form = forms.AuthorForm(request.POST)
        context = {'form_for_author': self.form_class}

        if form.is_valid():
            form.save()
            return redirect(reverse('author-list'))
        else:
            return render(request, self.template_name, context)


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'catalog/author_update.html'
    form_class = forms.AuthorForm

    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        form = forms.AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect(reverse('author-list'))
        else:
            form = forms.AuthorForm(instance=author)
            context = {
                'form': form}
        return render(request, self.template_name, context)


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'catalog/author_delete.html'

    def post(self, request, pk):
        query = request.POST.get("question", None)
        author = self.model.objects.get(id=pk)
        list_books = author.book_set.all()
        if query == "no":
            context = {
                'name': author.name,
                'surname': author.surname,
                'list_books': list_books}
            return render(request, self.template_name, context)
        author.delete()
        return redirect(reverse('author-list'))


class TegListView(ListView):
    model = Teg
    template_name = 'catalog/teg_list.html'
    context_object_name = 'tegs'

    def get(self, request, fltr):
        if fltr == "all":
            self.object_list = Teg.objects.all()
        elif fltr == "active":
            self.object_list = Teg.objects.filter(flag=True)
        elif fltr == "nonactive":
            self.object_list = Teg.objects.filter(flag=False)
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, fltr):
        query = request.POST['search']
        result_list = Teg.objects.filter(title=query)

        if result_list.count() != 0:
            alert = 'Результат фильтрации по названию теэга ' + query
            context = {
                'all_tegs': result_list,
                'query': alert}
        else:
            alert = 'Нет тэга с названием ' + query
            context = {
                'query': alert}
        return render(request, self.template_name, context)


class TegCreateView(LoginRequiredMixin, CreateView):
    model = Teg
    template_name = 'catalog/teg_create.html'
    form_class = forms.TegForm

    def post(self, request):
        form = forms.TegForm(request.POST)
        context = {
            'form_for_teg': self.form_class}
        if form.is_valid():
            form.save()
            return redirect(reverse('teg-list'))
        return render(request, self.template_name, context)


class TegUpdateView(LoginRequiredMixin, UpdateView):
    model = Teg
    template_name = 'catalog/teg_update.html'
    form_class = forms.TegForm

    def post(self, request, pk):
        teg = get_object_or_404(Teg, pk=pk)
        form = forms.TegForm(request.POST, instance=teg)
        if form.is_valid():
            teg = form.save(commit=False)
            teg.save()
            return redirect(reverse('teg-list'))
        else:
            form = forms.TegForm(instance=teg)
            context = {
                'form': form}
        return render(request, self.template_name, context)


class TegDeleteView(LoginRequiredMixin, DeleteView):
    model = Teg

    def post(self, request, id):
        teg = Teg.objects.get(id=id)
        teg.delete()
        return redirect(reverse('teg-list'))


class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'

    def get(self, request, search):
        authors_list = Author.objects.all()
        tegs_list = Teg.objects.all()
        if search == 'list':
            self.object_list = self.model.objects.all()
            context = {
                'all_tegs': tegs_list,
                'all_authors': authors_list,
                'all_books': self.object_list}
            return render(request, self.template_name, context)
        elif search == 'search':
            query = request.GET['search']
            self.object_list = self.model.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query))
            context = {
                'all_tegs': tegs_list,
                'all_authors': authors_list,
                'all_books': self.object_list}
        elif search != 'list':

            self.object_list = self.model.objects.filter(
                Q(author__surname=search) | Q(teg__title=search))
            context = {
                'all_tegs': tegs_list,
                'all_authors': authors_list,
                'all_books': self.object_list}
        return render(request, self.template_name, context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'catalog/book_create.html'
    form_class = forms.BookForm

    def post(self, request):
        form = forms.BookForm(request.POST)
        context = {'form_class': self.form_class}
        if form.is_valid():
            form.save()
            return redirect(reverse('book-list', args=['list']))
        else:
            return render(request, self.template_name, context)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'catalog/book_update.html'
    form_class = forms.BookForm

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = forms.BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect(reverse('book-list', args=['list']))
        else:
            form = forms.BookForm(instance=book)
            context = {
                'form': form}
        return render(request, self.template_name, context)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book

    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return redirect(reverse('book-list', args=['list']))


class AuthorCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializers


class AuthorListAPIView(generics.ListAPIView):
    serializer_class = AuthorListSerializers
    queryset = Author.objects.all()


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializers
    queryset = Author.objects.all()


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookDetailSerializers


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookListSerializers
    queryset = Book.objects.all()


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializers
    queryset = Book.objects.all()


class TegCreateAPIView(generics.CreateAPIView):
    serializer_class = TegDetailSerializers


class TegListAPIView(generics.ListAPIView):
    serializer_class = TegListSerializers
    queryset = Teg.objects.all()


class TegDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TegDetailSerializers
    queryset = Teg.objects.all()


class TegUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = TegUpdateSerializers
    queryset = Book.objects.all()
