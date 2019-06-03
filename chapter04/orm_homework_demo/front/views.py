from django.db import connection
from django.db.models import Avg, Count, Sum, Q
from django.shortcuts import render
from .models import Student,Course,Teacher,Score
from django.http import HttpResponse


def index(request):
    #1.查询平均成绩大于60分的同学的id和平均成绩
    results = Student.objects.annotate(avg_number=Avg("score__number")).filter(avg_number__gt=60).values("id","avg_number")
    # for result in results:
    #     print("%s:%s"%(result.name,result.score_set.number))
    #     print(connection.queries)
    for result in results:
        print(result)

    print(connection.queries)
    return HttpResponse("success")

def index2(request):
    #2.查询所有同学的id、姓名、选课的数、总成绩
    results = Student.objects.annotate(course_count=Count("score__course_id"),sum_score=Sum("score__number")).values("id","name","course_count","sum_score")
    for result in results:
        print(result)
    print(connection.queries)
    return HttpResponse("success")

def index3(request):
    #3.查询姓李的老师的个数
    # results = Teacher.objects.filter(name__startswith="李").aggregate(teacher_num=Count("id"))
    # print("teacher_num:%s"%(results["teacher_num"]))
    count = Teacher.objects.filter(name__startswith="李").count()
    print("teacher_num:%s"%count)
    print(connection.queries)
    return HttpResponse("success")

def index4(request):
    #4.查询没学过"李老师"课的同学的id、姓名
    results = Student.objects.exclude(score__course__teacher__name="李").values("id","name")
    for result in results:
        print(result)
    print(connection.queries)
    return HttpResponse("success")

def index5(request):
    #5.查询学过课程id为1和2的所有同学的id、姓名
    results = Student.objects.filter(score__course__in=[1,2]).values("id","name").distinct()
    for result in results:
        print(result)
    return HttpResponse("success")

def index6(request):
    #6.查询学过黄老师所交的所有课的同学的id、姓名
    # results = Student.objects.filter(score__course__teacher__name="黄").values("id","name")
    # for result in results:
    #     print(result)
    # print(connection.queries)
    # return HttpResponse("success")
    #查询黄老师所交的课程数量
    # results = Teacher.objects.filter(name__startswith="李").aggregate(count_num=Count("course"))
    # for result in results:
    #     print("count_num")
    # print(connection.queries)
    # return HttpResponse("success")

    #1.首先先找到每一位学生学习的黄老师课程的数量
    #2.在课程表中找到黄老师教的课程的数量
    #3.判断A是否等于B,如果相等，那么意味着这位学生学习了黄老师教的所有课程，如果不相等，那么意味着这位学生没有学完黄老师
    #教的所有课程
    # students = Student.objects.annotate(course_num=Count("score__course",filter=Q(score__course__teacher__name='黄老师'))).filter(course_num=Course.objects.filter(teacher__name="黄老师").count()).values("id","name")
    students = Student.objects.annotate(course_num=Count("score_course",filter=Q(score__course__teacher__name="黄老师"))).filter(Course.objects.filter(teacher__name="黄老师").count()).values("id","name")
    for student in students:
        print(student)
    return HttpResponse("success")

