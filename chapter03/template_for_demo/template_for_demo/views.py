from  django.shortcuts import render

def index(request):
    context = {
        "books" : [
            {
                "name":"三国演义",
                "author":"罗贯中",
                "price":199,
            },
            {
                "name":"水浒传",
                "author":"施耐庵",
                "price":109,
            },
            {
                "name":"西游记",
                "author":"吴承恩",
                "price":99,
            },
            {
                "name":"红楼梦",
                "author":"曹雪芹",
                "price":100,
            }
        ],
        "person":{
            "username":"zhiliao",
            "age":18,
            "height":180,
        },
        "comments":[
        ]

    }
    return render(request,"index.html",context=context)