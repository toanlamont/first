from django.shortcuts import render
from .models import Python
from .models import Sysadmin
from .models import Command
from .models import Lastest
from .models import ListJob
import lotto


# Create your views here.
def home(request):
    pyt = Python.objects.values()
    com = Command.objects.values()
    sys = Sysadmin.objects.values()
    las = Lastest.objects.values()
    c = ''
    if request.method=="POST":
        n = str(request.POST.get("num1"))
        c = lotto.check(n)
    return render(request, 'hv.html', {'pyts': pyt, 'coms': com, 'syss': sys, 'lass': las, 'c': c})
