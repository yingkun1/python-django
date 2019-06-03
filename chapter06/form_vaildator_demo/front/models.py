from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)
