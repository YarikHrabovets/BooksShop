from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Book, Genre, Page, UserBookList, Author


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'nickname', 'is_staff', 'is_active')
    list_filter = ('email', 'nickname', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'nickname', 'profile_pic', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email', 'password1', 'password2', 'is_staff',
                'is_active', 'groups', 'user_permissions'
            )}
         ),
    )
    search_fields = ('email', 'nickname')
    ordering = ('email', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('title', 'publication_date', 'genres')
    prepopulated_fields = {'slug': ('title', )}
    fieldsets = (
        (None, {'fields': ('title', 'author', 'description', 'publication_date', 'book_pic')}),
        ('Extra', {'fields': ('slug', 'genres')})
    )

    search_fields = ('title', 'author', )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_filter = ('book', 'page_number')


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_filter = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(UserBookList)
