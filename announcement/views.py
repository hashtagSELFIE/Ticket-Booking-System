from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Announcement
from account.models import Account, Announcer
from account.utils import prepare_context


# Create your views here.
def dashboard(request):
    context = prepare_context(request, show_navbar=True)

    context = {
        'show_navbar': True,
        'announcement': Announcement.objects.order_by("-announce_time")
    }
    return render(request, 'dashboard.html', context=context)
