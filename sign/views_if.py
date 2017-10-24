# -*- coding: utf-8 -*-
# @Time    : 17-10-24 下午9:42
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : views_if.py
# @Describe:
# @Software: PyCharm

from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist

#添加发布会接口

def add_event(request):
    eid = request.POST.get('eid','')
    name = request.POST.get('name','')
    limit = request.POST.get('limit','')
    status = request.POST.get('status','')
    address = request.POST.get('address','')
    start_time = request.POST.get('start_time','')

    if eid == '' or name=='' or limit =='' or address == '' or start_time =='':
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exists'})
    if status=='':
        status = 1
    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error'
        return JsonResponse({'status':10024,'message':'error'})
    return JsonResponse({'status':200,'message':'add event success'})

# def get_event_list(request):
#     eid = request.GET.get('eid','')
#     name = request.GET.get('name','')
#
#     if
