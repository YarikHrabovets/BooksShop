from django.urls import path
from .views import index, RegisterUser, AuthoriseUser, Profile, BooksList, BookDetail, random_book, \
    add_book_to_list, del_from_book_list, logout_user, GenresList, GenreDetail, AuthorList, AuthorDetail

urlpatterns = [
    path('', index, name='index'),
    path('accounts/signup/', RegisterUser.as_view(), name='signup'),
    path('accounts/login/', AuthoriseUser.as_view(), name='login'),
    path('accounts/logout/', logout_user, name='logout'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('books/', BooksList.as_view(), name='books_list'),
    path('books/<slug:book_slug>/', BookDetail.as_view(), name='book_detail'),
    path('add-book/<int:pk>', add_book_to_list, name='add_book_to_list'),
    path('delete-book/<int:pk>', del_from_book_list, name='del_from_book_list'),
    path('genres/', GenresList.as_view(), name='genres_list'),
    path('genres/<slug:genre_slug>', GenreDetail.as_view(), name='genre_detail'),
    path('authors/', AuthorList.as_view(), name='authors_list'),
    path('authors/<slug:author_slug>', AuthorDetail.as_view(), name='author_detail'),
    path('random/', random_book, name='random')
]
