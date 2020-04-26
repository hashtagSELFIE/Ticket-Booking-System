from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Account


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ('gender', 'birth_date')
