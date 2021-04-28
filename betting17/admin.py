from django.contrib import admin
from .models import *


# Register your models here.


class MatchesAdmin(admin.ModelAdmin):
    list_display = ['id', 'league_country', 'league_title', 'home', 'away', 'odds_1', 'odds_x', 'odds_2', 'date', 'time', 'result']


admin.site.register(Matches, MatchesAdmin)


class TicketsAdmin(admin.ModelAdmin):
    list_display = ['id', 'odds_total', 'status', ]


admin.site.register(Tickets, TicketsAdmin)
