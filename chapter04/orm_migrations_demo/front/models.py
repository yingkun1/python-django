from django.db import models

class FrontUser(models.Model):
    username = models.CharField(max_length=100)
