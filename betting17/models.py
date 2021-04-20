from django.db import models


# Create your models here.
class Matches(models.Model):
    league_country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Država lige')
    league_title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Naziv lige')
    home = models.CharField(max_length=30, null=False, blank=False, verbose_name='Domaći')
    away = models.CharField(max_length=30, null=False, blank=False, verbose_name='Gosti')
    time = models.CharField(max_length=20, blank=True, null=True, verbose_name='Vrijeme početka')
    result = models.CharField(max_length=10, null=True, blank=True, verbose_name='rezultat')
    odds_1 = models.FloatField(verbose_name='1', null=True)
    odds_x = models.FloatField(verbose_name='2', null=True)
    odds_2 = models.FloatField(verbose_name='X', null=True)

    def __str__(self):
        return f'{self.home} - {self.away}'

    class Meta:
        verbose_name = 'Mečevi'
        verbose_name_plural = verbose_name


class Tickets(models.Model):
    matches = models.ManyToManyField(Matches, 'Parovi')
    odds_total = models.FloatField(null=True)
    status = models.CharField(max_length=10, null=False, blank=False,)
