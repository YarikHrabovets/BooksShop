from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.views.generic.list import MultipleObjectMixin

from random import choice

from .models import CustomUser, Book, UserBookList, Genre, Author
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm


class RegisterUser(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'books/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return super(RegisterUser, self).form_valid(user)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.id})


class AuthoriseUser(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.id})


class Profile(LoginRequiredMixin, generic.edit.UpdateView):
    model = CustomUser
    template_name = 'books/profile.html'
    context_object_name = 'user_profile'
    fields = ('profile_pic', )

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['form'] = CustomUserChangeForm(initial={'email': self.object.email})
        context['user_book_list'] = UserBookList.objects.get_or_create(user=self.object)[0].books.all()

        return context


class BooksList(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books_list'


class BookDetail(generic.DetailView, MultipleObjectMixin):
    model = Book
    template_name = 'books/book_detail.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        genres = self.object.genres.all()
        object_list = self.object.page_set.all()
        is_added = UserBookList.objects.filter(user=self.request.user.id, books=self.object.pk).exists()
        context = super(BookDetail, self).get_context_data(
            genres=genres,
            object_list=object_list,
            is_added=is_added,
            **kwargs
        )

        return context


class GenresList(generic.ListView):
    model = Genre
    template_name = 'books/genres_list.html'
    context_object_name = 'genres_list'


class GenreDetail(generic.DetailView):
    model = Genre
    template_name = 'books/genre_detail.html'
    slug_url_kwarg = 'genre_slug'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        context['books'] = Book.objects.filter(genres=self.object.pk)

        return context


class AuthorList(generic.ListView):
    model = Author
    template_name = 'books/authors_list.html'
    context_object_name = 'authors_list'


class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'books/author_detail.html'
    slug_url_kwarg = 'author_slug'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object.pk)

        return context


def index(request):
    lasted_books = Book.objects.order_by('-pk')[:3]
    return render(request, 'books/index.html', context={'lasted_books': lasted_books})


@login_required
def add_book_to_list(request, pk):
    user_book_list, created = UserBookList.objects.get_or_create(user=request.user)
    book = Book.objects.get(pk=pk)
    if pk not in (user_book.pk for user_book in user_book_list.books.all()):
        user_book_list.books.add(book)
        user_book_list.save()

    return redirect('book_detail', book_slug=book.slug)


@login_required
def del_from_book_list(request, pk):
    user_book_list, created = UserBookList.objects.get_or_create(user=request.user)
    book = Book.objects.get(pk=pk)
    if pk in (user_book.pk for user_book in user_book_list.books.all()):
        user_book_list.books.remove(book)

    return redirect('book_detail', book_slug=book.slug)


def random_book(request):
    books_slug = Book.objects.values_list('slug')
    if books_slug:
        random_slug = choice(books_slug)
        return redirect('book_detail', book_slug=random_slug[0])

    return redirect('books_list')


def logout_user(request):
    logout(request)
    return redirect('login')


def page_not_found_view(request, exception):
    return render(request, 'books/404.html', status=404)
