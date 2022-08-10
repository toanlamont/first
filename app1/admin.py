from django.contrib import admin
from .models import ListJob
from .models import Python
from .models import Command
from .models import Sysadmin
from .models import Lastest

# Register your models here.
class Host(admin.ModelAdmin):
    list_display = ('title', 'link')
admin.site.register(ListJob, Host)
admin.site.register(Python, Host)
admin.site.register(Command, Host)
admin.site.register(Sysadmin, Host)
admin.site.register(Lastest, Host)


