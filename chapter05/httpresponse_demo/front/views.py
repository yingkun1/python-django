from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

def index(request):
    # return HttpResponse("知了课堂")
    # response = HttpResponse()
    # response.content = "知了课堂"
    # return response
    response = HttpResponse("<h1>知了课堂</h1>",content_type="text/plain;charset=utf-8")
    response['PASSWORD'] = 'zhiliao'
    # response.status_code = 400
    return response

def jsonresponse_view(request):
    # person = {
    #     "username":"zhiliao",
    #     'age':18,
    #     'height':180,
    # }
    # person_str = json.dumps(person)
    # response = HttpResponse(person_str,content_type="application/json")
    # return response
    # response = JsonResponse(person)
    # return response
    # return JsonResponse(person)
    persons = [
        {
            "username":"zhiliao",
            "age":18,
            "height":180,
        },
        {
            "username":"xiaozhang",
            "age":20,
            "height":173,
        }
    ]
    return JsonResponse(persons,safe=False)