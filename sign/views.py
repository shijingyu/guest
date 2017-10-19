# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from sign.models import Event, Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):
   # return HttpResponse("Hello World")
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user) #登录

        #if username == 'admin' and password == 'admin123':
            #return HttpResponse('login success!')
            #return HttpResponseRedirect('/event_manage/')
            respone = HttpResponseRedirect('/event_manage/')
            #respone.set_cookie('user',username,3600)
            request.session['user'] = username
            return respone

        else:
            return render(request,'index.html',{'error':'username or password error!'})
    else:
        return HttpResponse('login error!')

@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'event_manage.html',{"user":username, "events":event_list})

@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user":username, "events":event_list})

@login_required
def guest_manage(request):
    username =request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2) # 每页显示2条数据
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)

    except PageNotAnInteger:
        #如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user":username, "guests":contacts})

@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event,id=eid)
    return render(request, 'sign_index.html', {'event':event})
