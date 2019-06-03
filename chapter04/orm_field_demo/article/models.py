from django.db import models
from django.utils.timezone import now

class Article(models.Model):
    #如果想要使用自己定义的Field来作为主键，那么必须设置primary_key=True
    id = models.BigAutoField(primary_key=True)
    #在定义字段的时候，如果没有指定null=True，那么默认情况下,null=False
    #即不能为空
    #如果想要使用可以为null的BooleanField，那么应该使用NullBooleanField来替代
    remove = models.NullBooleanField()
    #CharField:如果超过了254个字符，那么就不建议使用了，推荐使用TextField:longtext
    title = models.CharField(max_length=200)
    #auto_now_add:是在第一次添加数据进去的时候会自动获取当前的时间
    #auto_now:每次这个对象调用save方法的时候都会将当前的时间更新
    create_time = models.DateTimeField(auto_now=True)

class Person(models.Model):
    email = models.EmailField()
    signature = models.TextField()

class Author(models.Model):
    username = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True,db_column="author_age",default=0)
    create_time = models.DateTimeField(default=now)
    telephone = models.CharField(max_length=11,unique=True,null=True)

    def __str__(self):
        return "<(Author id:%s,create_time:%s)>"%(self.id,self.create_time)

    class Meta:
        db_table = "author"
        ordering = ["-create_time","id"]