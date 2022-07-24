import requests
from bs4 import BeautifulSoup
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
    c = ''
    results = []
    r = requests.get("http://ketqua1.net")
    tree = BeautifulSoup(markup=r.text)
    nodes = tree.find_all(name="td", attrs={"class": "chu17"})

    for node in nodes:
        results.append(node.text)
    if request.method == "POST":
        n = str(request.POST.get('num1'))
        if n in results:
            c = 'Bạn đã trúng lô'
        elif n.isspace() is True:
            c = " "
        else:
            c = 'Bạn đã tạch lô'
    return render(request, 'familug.html', {'pythons': pyt, 'commands': com, 'syss': sys, "lass":las, "c":c})



