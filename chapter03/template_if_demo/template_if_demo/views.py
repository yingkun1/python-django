from django.shortcuts import render

def index(request):
    # context = {
    #     "age":17
    # }
    context = {
        "heros":[
            # '鲁班一号',
            '项羽',
            '程咬金',
        ]
    }
    return render(request,'index.html',context=context)