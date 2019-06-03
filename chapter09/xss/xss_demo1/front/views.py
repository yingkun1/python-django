from django.shortcuts import render,redirect,reverse
from .models import Comment
from django.views.decorators.http import require_http_methods
from django.template.defaultfilters import escape
import bleach
from bleach.sanitizer import ALLOWED_TAGS,ALLOWED_ATTRIBUTES

def index(request):
    context = {
        'comments':Comment.objects.all()
    }
    return render(request,"index.html",context=context)

@require_http_methods(['POST'])
def add_comment(request):
    content = request.POST.get('content')
    # content = escape(content)
    tags = ALLOWED_TAGS + ['img']
    attributes = {**ALLOWED_ATTRIBUTES,'img':['src']}
    cleaned_data = bleach.clean(content,tags=tags,attributes=attributes)
    Comment.objects.create(content=cleaned_data)
    return redirect(reverse('index'))