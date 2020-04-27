import django.forms as forms
from django.contrib.auth.models import User
from .models import Account


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('gender', 'birth_date')
