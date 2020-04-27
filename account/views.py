from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from .models import Account
from .forms import AccountForm, RegisterForm


# Create your views here.
class LoginView(View):
    def get(self, request):
        context = {
            'show_navbar': True
        }
        return render(request, 'account/login.html', context=context)

    def post(self, request):
        context = {
            'show_navbar': True
        }
        username = request.POST.get('user')
        pwd = request.POST.get('password')
        if username and pwd:
            user = authenticate(username=username, password=pwd)
            if user:
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
        context = {
            'show_navbar': True
        }

        register_form = RegisterForm()
        context['register_form'] = register_form
        return render(request, 'account/signup.html', context=context)

    def post(self, request):
        context = {
            'show_navbar': True
        }

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
                print(hasUser)
                if not hasUser:
                    user = User.objects.create_user(
                        data_form['email'],
                        email=data_form['email'],
                        password=data_form['password'],
                        first_name=data_form['first_name'],
                        last_name=data_form['last_name']
                    )
                    user.groups.set(['passenger'])
                    user.save()

                    account = Account(user_id=user, user_type='US')
                    account.save()

                    return redirect('/')
                else:
                    context['error'] = {
                        'errorMsg': 'Email have been used!'
                    }

        context['register_form'] = register_form
        return render(request, 'account/signup.html', context=context)
