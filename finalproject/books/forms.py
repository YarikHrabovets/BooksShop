from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import AuthenticationForm
from django import forms
from captcha.fields import CaptchaField

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password confirmation'

    class Meta:
        model = CustomUser
        fields = ('email', 'nickname', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('profile_pic', )
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'required': ''})
        }


class CustomAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
