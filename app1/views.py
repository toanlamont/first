
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import ListJob
from .models import python
from .models import command
from .models import sysadmin
from .models import lastest


# Create your views here.
def trang_chu(request):
    return HttpResponse('Hello pymier')
def binh_phuong(request, n):
    r = n ** 2
    return HttpResponse("Ket qua: {}".format(r))
def up(request, name):
    return HttpResponse('hello {}'.format(name.upper()))
data = {'name': 'pymi2205',
'year': 2022,
'student': ['Hang', 'Nhu', 'Huyen']}


def student(request):
    return JsonResponse(data)



def jobs(request):
    title = ListJob.objects.values()
    return render(request, "index.html", {'titles': title})

def familug(request):
    pyt = python.objects.values()
    com = command.objects.values()
    las = lastest.objects.values()
    sys = sysadmin.objects.values()
    return render(request, 'familug.html', {'pythons': pyt, 'commands': com, 'syss': sys, "lass":las})


