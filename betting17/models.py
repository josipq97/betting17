from django.db import models


# Create your models here.
class Matches(models.Model):
    home = models.CharField(max_length=30, null=False, blank=False, verbose_name='Domaći')
    away = models.CharField(max_length=30, null=False, blank=False, verbose_name='Gosti')
    time = models.DateTimeField(verbose_name='Vrijeme početka')
    result = models.CharField(max_length=10, verbose_name='rezultat')

    def __str__(self):
        return f'{self.home} - {self.away}'

    class Meta:
        verbose_name = 'Mečevi'
        verbose_name_plural = verbose_name


class Tickets(models.Model):
    match = models.ManyToManyField(Matches, on_delete=models.CASCADE)
    ods_total = models.FloatField()
    status = models.CharField(max_length=10, null=False, blank=False)
