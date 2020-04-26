from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .forms import RegisterForm


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html', context={
            'show_navbar': True
        })

    def post(self, request):
        username = request.POST.get('user')
        pwd = request.POST.get('password')
        if username and pwd:
            user = authenticate(username=username, password=pwd)
            if user:
                return redirect('/')

        return render(request, 'account/login.html', context={
            'show_navbar': True
        })


class SignupView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'account/signup.html', context={
            'show_navbar': True,
            'register_form': register_form
        })

    def post(self, request):
        return HttpResponse('test login')
