from django import template
from datetime import datetime

register = template.Library()

#过滤器最多只能有两个参数
#过滤器的第一个参数永远都是被过滤的那个参数(也就是竖线左边的那个参数)
@register.filter("my_greet")
def greet(value,word):
    return value + word

# register.filter("greet",greet)
@register.filter
def time_since(value):
    """
    time距离现在的时间间隔
    1.
    如果时间间隔小于1分钟，那么就显示刚刚
    2.
    如果大于1分钟小于1小时，那么就显示xx分钟前
    3.
    如果是大于1小时小于24小时，那么就显示xx小时前
    4.
    如果是大于24小时小于30天以内，那么就显示xx天前
    5.
    否则就是显示具体的时间
    """
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    #timedelay.total_seconds
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return "刚刚"
    elif timestamp >=60 and timestamp < 60*60:
        minutes = int(timestamp/60)
        return("%s分钟之前"%minutes)
    elif timestamp >=60*60 and timestamp < 3600*24:
        hours = int(timestamp/3600)
        return("%s小时之前"%hours)
    elif timestamp >= 3600*24 and timestamp < 3600*24*30:
        days = int(timestamp/3600/24)
        return("%s天之前"%days)
    else:
        return value.strftime("%Y/%m%d %H%M")
