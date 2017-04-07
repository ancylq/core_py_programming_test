# coding: utf-8
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
# 使用render可以不导入下列包
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt 

from blog.models import BlogPost
from blog.forms import BlogPostForm
# Create your views here.

@csrf_exempt # 关闭csrf，但实验不管用
def context_render(request, tpl, data={}):
    '''等同于render()会自动使用RequestContext'''
    return render_to_response(tpl, data, context_instance=RequestContext(request))

def archive(request):
    post = BlogPost.objects.all()[:10] # 将order_by('-timestemp')移到了models.py中
#     return context_render(request, 'archive.html', {'posts':post,
#                                                     'form':BlogPostForm()})
    return render(request, 'archive.html', {'posts':post,
                                            'form':BlogPostForm()})

def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 并不会真正保存数据
            post.timestemp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')

