from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.FloatField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
