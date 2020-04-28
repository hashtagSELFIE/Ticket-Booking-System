from django.contrib import admin

from account.models import Account, Announcer, TicketSeller

# Register your models here.

admin.site.register(Account)

admin.site.register(Announcer)

admin.site.register(TicketSeller)
