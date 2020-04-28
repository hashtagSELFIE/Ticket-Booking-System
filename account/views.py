from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User, Group
from .models import Account
from .forms import AccountForm, RegisterForm
from .utils import prepare_context


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/')


class LoginView(View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        return render(request, 'account/login.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        username = request.POST.get('user')
        pwd = request.POST.get('password')
        if username and pwd:
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context['error'] = {
                    'errorMsg': "Username or password mismatch or not found!"
                }
        elif username or pwd:
            context['error'] = {
                'errorMsg': "Missing username or password"
            }
        return render(request, 'account/login.html', context=context)


class SignupView(View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        register_form = RegisterForm()
        context['register_form'] = register_form
        return render(request, 'account/signup.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        repassword = request.POST.get('repassword')
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            data_form = register_form.clean()
            print(data_form)
            print(data_form['password'], repassword)

            if data_form['password'] != repassword:
                context['error'] = {
                    'errorMsg': 'Password mismatch!'
                }
            else:
                hasUser = User.objects.filter(email__exact=data_form['email'])
                if not hasUser:
                    user = User.objects.create_user(
                        data_form['email'],
                        email=data_form['email'],
                        password=data_form['password'],
                        first_name=data_form['first_name'],
                        last_name=data_form['last_name']
                    )

                    passenger_group = Group.objects.get(name='passenger')
                    passenger_group.user_set.add(user)

                    user.save()
                    passenger_group.save()

                    account = Account(user_id=user, user_type='US')
                    account.save()

                    return redirect('/login')
                else:
                    context['error'] = {
                        'errorMsg': 'Email have been used!'
                    }

        context['register_form'] = register_form
        return render(request, 'account/signup.html', context=context)


class EditView(LoginRequiredMixin, View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        account_form = AccountForm()
        context['account_form'] = account_form
        register_form = RegisterForm()
        context['register_form'] = register_form
        user = request.user
        context['user'] = user
        account = Account.objects.get(user_id_id=user.id)
        context['account'] = account

        return render(request, 'account/edit.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        register_form = RegisterForm(request.POST)
        account_form = AccountForm(request.POST)

        if register_form.is_valid() or account_form.is_valid():
            cleaned_register = register_form.clean()
            cleaned_account = account_form.clean()
            print(cleaned_account, cleaned_register)

            user = request.user
            usernew = User.objects.get(pk=user.id)
            usernew.first_name = cleaned_register['first_name']
            usernew.last_name = cleaned_register['last_name']

            account = Account.objects.get(user_id_id=user.id)
            account.gender = cleaned_account['gender']
            account.birth_date = cleaned_account['birth_date']

            usernew.save()
            account.save()

            return redirect('/')

        context['register_form'] = register_form
        context['account_form'] = account_form

        return render(request, 'account/edit.html', context=context)
