from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
from tinymce import models as tinymce_models

import os
from PIL import Image

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    nickname = models.CharField(_('Nickname'), max_length=30)
    profile_pic = models.ImageField(_('Profile picture'), null=True, blank=True, upload_to='imgs/profile/')
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = CustomUser.objects.get(pk=self.pk)

            if old_instance.profile_pic != self.profile_pic:
                if old_instance.profile_pic and os.path.isfile(old_instance.profile_pic.path):
                    os.remove(old_instance.profile_pic.path)

        super().save(*args, **kwargs)
        if self.profile_pic:
            img = Image.open(self.profile_pic)
            img = img.resize((300, 300), Image.LANCZOS)
            img.save(self.profile_pic.path, quality=100)
            img.close()
            self.profile_pic.close()


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(_('URL'), max_length=255, unique=True)
    biography = tinymce_models.HTMLField(_('Biography'))
    author_pic = models.ImageField(_('Picture'), null=True, blank=True, upload_to='imgs/authors/')

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'author_slug': self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(_('URL'), max_length=255, unique=True)
    description = tinymce_models.HTMLField(_('Description'))

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'genre_slug': self.slug})


class Book(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('URL'), max_length=255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    description = tinymce_models.HTMLField(_('Description'))
    genres = models.ManyToManyField(Genre)
    book_pic = models.ImageField(_('Picture'), null=True, blank=True, upload_to='imgs/books/')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_slug': self.slug})


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    content = tinymce_models.HTMLField(_('Content'))

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return f'Page {self.page_number} of {self.book}'


class UserBookList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.user}'s Book List"
