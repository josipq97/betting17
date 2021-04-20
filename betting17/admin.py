from django.contrib import admin
from .models import *


# Register your models here.


class MatchesAdmin(admin.ModelAdmin):
    list_display = ['id', 'home', 'away', 'ods_1', 'ods_x', 'ods_2', 'time', 'result']


admin.site.register(Matches, MatchesAdmin)


class TicketsAdmin(admin.ModelAdmin):
    list_display = ['id', 'ods_total', 'status', ]


admin.site.register(Tickets, TicketsAdmin)
