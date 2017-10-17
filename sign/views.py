# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
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
    username = request.session.get('user','')
    return render(request,'event_manage.html',{"user":username})
