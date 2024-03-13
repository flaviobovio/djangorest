""" class models """
from django.db import models
from django.utils import timezone

class Swimmer(models.Model):
    """ swimmer model """
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField()
    club = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.name)} ({self.age}) - {self.club}'


class Date(models.Model):
    """ Date Model """
    date = models.DateField(default=timezone.now ,blank=False, null=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)
    
class Mark(models.Model):
    """ Mark Model """
    swimmer = models.ForeignKey(Swimmer.id, on_delete=models.CASCADE, default=0)
    date = models.ForeignKey(Date.id, on_delete=models.CASCADE, default=0)
    meters = models.FloatField(blank=False, null=False)

    def __str__(self):
        return ''#f'{self.swimmer} - {self.date} - {self.meters}'

