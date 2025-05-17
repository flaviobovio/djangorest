""" class models """
from django.db import models
from django.utils import timezone

class Club(models.Model):
    """" club model """
    name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.city}'

class Swimmer(models.Model):
    """ swimmer model """
    SEX_CHOICES = [        
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]

    name = models.CharField(max_length=100, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)    
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)    
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
        return f'{self.date} - {"Active" if self.active else "Inactive"}'

class Mark(models.Model):
    """ Mark Model """
    swimmer = models.ForeignKey(Swimmer, on_delete=models.CASCADE, default=None)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None)
    meters = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.swimmer} - {self.date} - {self.meters}'
