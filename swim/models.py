""" class models """
from django.db import models
from django.utils import timezone

class Category(models.Model):
    """" category model """
    name = models.CharField(max_length=100, blank=False, null=False)
    age_min = models.IntegerField(blank=False, null=False)
    age_max = models.IntegerField(blank=False, null=False)
    
    def __str__(self):
        return f'{self.name} ({self.age_min}-{self.age_max})'

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
    identification = models.CharField(max_length=20, default='')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)    
    age = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)      
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)    
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.name)} ({self.age}) - {self.club}'


class Date(models.Model):
    """ Date Model """
    name = models.CharField(max_length=100, blank=False, null=False, default='')
    date = models.DateField(default=timezone.now ,blank=False, null=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.date} - {"Active" if self.active else "Inactive"}'

class Mark(models.Model):
    """ Mark Model """
    swimmer = models.ForeignKey(Swimmer, on_delete=models.CASCADE, default=None)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, default=None)
    meters = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f'{self.swimmer} - {self.date} - {self.meters}'
