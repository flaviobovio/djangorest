""" class models """
from django.db import models


class Swimmer(models.Model):
    """ swimmer model """
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField()
    club = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.name)} ({self.age}) - {self.club}'
