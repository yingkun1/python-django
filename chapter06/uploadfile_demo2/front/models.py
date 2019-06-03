from django.db import models
from django.core import validators

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnail = models.FileField(upload_to='media')
    # thumbnail = models.FileField(upload_to='%Y/%m/%d',validators=[validators.FileExtensionValidator(['txt'],message='thumbnail必须为.txt格式的文件!')])
    thumbnail = models.ImageField(upload_to='%Y/%m/%d')
