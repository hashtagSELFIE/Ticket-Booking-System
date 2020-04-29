from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from account.utils import prepare_context
from account.models import Account
from booking.models import Ticket
from schedule.models import Timetable, Station, Train


class ViewTransaction(LoginRequiredMixin, View):
    def get(self, request):
        context = prepare_context(request, show_navbar=True)
        user = request.user
        context['user'] = user
        account = Account.objects.get(user_id_id=user.id)
        if account.user_type == 'TS':
            context['ticket'] = Ticket.objects.all()
            context['is_TS'] = True
        else:
            context['ticket'] = Ticket.objects.filter(buyer_id=account.id)

        context['schedule'] = Timetable.objects.all()
        context['station'] = Station.objects.all()
        context['train'] = Train.objects.all()

        return render(request, 'transaction/viewTransaction.html', context=context)

    def post(self, request):
        return HttpResponse(200)


class EditTransaction(LoginRequiredMixin, View):
    def get(self, request, announcement_id):
        context = prepare_context(request, show_navbar=True)
        # context['announcement'] = Announcement.objects.get(pk=announcement_id)
        # return render(request, 'transaction/editTransaction.html', context=context)
        return HttpResponse(200)

    def post(self, request, announcement_id):
        context = prepare_context(request, show_navbar=True)
        # announcement = Announcement.objects.get(pk=announcement_id)
        text = request.POST.get('announce_text')
        count = request.POST.get('view_count')
        #
        # if text != announcement.announce_text:
        #     announcement.announce_text = text
        #
        # if count != announcement.view_count:
        #     announcement.view_count = count
        #
        # announcement.announce_time = datetime.now()
        # announcement.save()

        return redirect('/transaction/')


@login_required()
def DeleteTransaction(request, announcement_id):
    # announcement = Announcement.objects.get(pk=announcement_id)
    # announcement.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
