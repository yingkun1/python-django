from django.db import models

#如果要将一个普通的类变成一个可以映射到数据库中的orm模型
#那么必须要将父类设置为models.Model或者它的子类
class Book(models.Model):
    #1.id:int类型，是自动增长的，主键
    id = models.AutoField(primary_key=True)
    #2.name:varchar类型，最大长度100，不能为空
    name = models.CharField(max_length=100,null=False)
    #3.author:varchar类型，最大长度为100，不能为空
    author = models.CharField(max_length=100,null=False)
    #4.price:float类型，不能为空，默认值为0
    price = models.FloatField(null=False,default=0)

class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)


