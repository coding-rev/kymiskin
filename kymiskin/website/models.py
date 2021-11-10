from django.conf import settings
from django.db import models
from django.shortcuts import reverse


from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

SERVICE_CHOICES =[
    ('Skin', 'Skin Care Treatment'),
    ('Body', 'Body Treatment'),
    ('Weight', 'Weight Management'),
]

class Appointments(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    service = models.CharField(choices=SERVICE_CHOICES, max_length=100)
    date = models.DateTimeField()
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'APPOINTMENTS'

    def __str__(self):
        return self.name