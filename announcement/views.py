from django.shortcuts import render
from announcement.models import Announcement


# Create your views here.
def dashboard(request):
    context = {
        'show_navbar': True,
        'announcement': Announcement.objects.order_by("announce_time")
    }
    return render(request, 'dashboard.html', context=context)
