from django.shortcuts import render
from app01.models import Course,DegreeCourse,PricePolicy,ContentType
from django.http import HttpResponse

# Create your views here.
def test(request):
    # degree_obj = DegreeCourse.objects.filter(title="python全栈").first()
    # content_type_obj = ContentType.objects.filter(model="degreecourse").first()
    # PricePolicy.objects.create(price=9.9,period=30,object_id=degree_obj.id,content_type_id=content_type_obj.id)
    # return HttpResponse("success")

    #为学位课"python全栈"添加价格策略
    # degree_obj1 = DegreeCourse.objects.filter(title="python全栈").first()
    # PricePolicy.objects.create(price=10,period=60,content_object=degree_obj1)
    #
    # degree_obj2 = DegreeCourse.objects.filter(title="python全栈").first()
    # PricePolicy.objects.create(price=20, period=60, content_object=degree_obj2)
    #
    # degree_obj3 = DegreeCourse.objects.filter(title="python全栈").first()
    # PricePolicy.objects.create(price=30, period=60, content_object=degree_obj3)
    # return HttpResponse("success")

    #为普通课"rest framework"添加价格策略
    # course_obj1 = Course.objects.filter(title="rest framewrok").first()
    # PricePolicy.objects.create(price=1,period=10,course_obj=course_obj1)
    # return HttpResponse("success")

    # degree_obj3 = Course.objects.filter(title="rest framework").first()
    # PricePolicy.objects.create(price=30, period=60, content_object=degree_obj3)
    # return HttpResponse("success")

    #3.根据课程id获取课程，并获取该课程的所有价格策略
    course = Course.objects.filter(id=1).first()
    price_policys = course.price_policy_list.all()
    print(price_policys)
    return HttpResponse("success")