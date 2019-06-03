from django.db import models
from django.core import validators

class Book(models.Model):
    title = models.CharField(max_length=100)
    page = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=1000)])

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[345678]\d{9}')])
