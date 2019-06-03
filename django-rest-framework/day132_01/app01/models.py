from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType


class Course(models.Model):
    """
    普通课程
    """
    title = models.CharField(max_length=12)
    #仅用于反向查找
    price_policy_list = GenericRelation("PricePolicy")

class DegreeCourse(models.Model):
    """
    学位课程
    """
    title = models.CharField(max_length=32)
    # 仅用于反向查找
    price_policy_list = GenericRelation("PricePolicy")


class PricePolicy(models.Model):
    """
    价格策略
    """
    price = models.IntegerField()
    period = models.IntegerField()

    content_type = models.ForeignKey(ContentType,verbose_name='关联表的名称',on_delete=models.DO_NOTHING)
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID')
    #帮助你快速实现content_type操作
    content_object = GenericForeignKey('content_type','object_id')