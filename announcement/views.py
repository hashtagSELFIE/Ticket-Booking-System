from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View

from .models import Announcement
from .forms import AnnouncementForm
from account.models import Account, Announcer
from account.utils import prepare_context
from schedule.models import Station


# Create your views here.
def dashboard(request):
    context = prepare_context(request, show_navbar=True)

    context = {
        'show_navbar': True,
        'announcement': Announcement.objects.order_by("-announce_time"),
        'stations': Station.objects.all()
    }
    return render(request, 'dashboard.html', context=context)


class ViewAnnouncement(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'announcement.view_announcement'

    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = request.user
        context['user'] = user
        account = Account.objects.get(user_id_id=user.id)

        # announcer = Announcer.objects.get(user_id=account.id)
        context['announcement'] = Announcement.objects.all()
        context['is_announcer'] = account.user_type == 'AN'

        return render(request, 'announcement/viewAnnouncement.html', context=context)


class CreateAnnouncement(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'announcement.add_announcement'

    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = request.user
        # announcer = Announcer.objects.get(user_id=account.id)
        context['announcement'] = Announcement.objects.filter(
            announcer_user_id=account.id)

        context['user'] = user
        announcement_form = AnnouncementForm()
        context['announcement_form'] = announcement_form

        return render(request, 'announcement/createAnnouncement.html', context=context)

    def post(self, request):
        context = prepare_context(request, show_navbar=True)
        annoucement_form = AnnouncementForm(request.POST)
        user = request.user
        account = Account.objects.get(user_id_id=user.id)

        if annoucement_form.is_valid():
            data_form = annoucement_form.clean()

            if data_form['announce_text'] is None:
                context['error'] = {
                    'errorMsg': 'Please fill in the announcement form'
                }
            else:
                announcement = Announcement.objects.create(
                    announce_text=data_form['announce_text'],
                    announce_time=datetime.now(),
                    view_count=0,
                    announcer_user_id=account.id
                )

                announcement.save()
                return redirect('/announcement/')

        context['announcement_form'] = annoucement_form
        return render(request, 'announcement/createAnnouncement.html', context=context)


class EditAnnouncement(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'announcement.change_announcement'

    def get(self, request, announcement_id):
        context = prepare_context(request, show_navbar=True)
        # announcer = Announcer.objects.get(user_id=account.id)
        announcement_form = AnnouncementForm()
        context['announcement_form'] = announcement_form
        context['announcement'] = Announcement.objects.get(
            pk=announcement_id)
        return render(request, 'announcement/editAnnouncement.html', context=context)

    def post(self, request, announcement_id):
        context = prepare_context(request, show_navbar=True)
        announcement = Announcement.objects.get(pk=announcement_id)
        text = request.POST.get('announce_text')
        count = request.POST.get('view_count')

        if text != announcement.announce_text:
            announcement.announce_text = text

        if count != announcement.view_count:
            announcement.view_count = count

        announcement.announce_time = datetime.now()
        announcement.save()

        return redirect('/announcement/')


@login_required()
@permission_required('announcement.delete_announcement')
def DeleteAnnouncement(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    announcement.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
