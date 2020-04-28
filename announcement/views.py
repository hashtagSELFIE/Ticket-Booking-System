from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Announcement
from account.utils import prepare_context


# Create your views here.
def dashboard(request):
    context = prepare_context(request, show_navbar=True)

    announcements = Announcement.objects.all().order_by("announce_time")
    print("announcement", announcements)
    context = {
        'show_navbar': True,
        'announcement': Announcement.objects.order_by("announce_time")
    }
    return render(request, 'dashboard.html', context=context)
