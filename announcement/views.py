from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View

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


class ViewAnnouncement(LoginRequiredMixin, View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = request.user
        context['user'] = user
        account = Account.objects.get(user_id_id=user.id)
        # announcer = Announcer.objects.get(user_id=account.id)
        context['announcement'] = Announcement.objects.filter(announcer_user_id=account.id)

        return render(request, 'announcement/viewAnnouncement.html', context=context)

    def post(self, request):
        return HttpResponse(200)


class EditAnnouncement(LoginRequiredMixin, View):
    def get(self, request):
        return None

    def post(self, request):
        return None


@login_required()
def DeleteAnnouncement(announcement_id, request):
    if request.method == 'POST':
        Announcement.objects.get(pk=announcement_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
