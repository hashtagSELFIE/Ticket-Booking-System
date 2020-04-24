from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class AuthentificationView(View):
    def get(self, request):
        return render(request, 'base.html', context={})

    def post(self, request):
        return HttpResponse('test login')
