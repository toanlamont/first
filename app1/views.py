import re
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
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

import json
def student(request):
    return JsonResponse(data)
def index(request):
    return HttpResponse("""
    <html><head><title>mywebsite</title></head>
    <body><h1>Day la trang chu Pymi
    </body>
    </html>
    """)
