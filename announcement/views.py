from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Announcement


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


def prepare_context(request, show_navbar=True):
    context = {
        'show_navbar': show_navbar
    }

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        context['current_user'] = user

    return context
