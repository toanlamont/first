from django.contrib import admin

# Register your models here.
from .models import ListJob
from .models import python
from .models import command
from .models import lastest
from .models import sysadmin

class HostListJob(admin.ModelAdmin):
    list_display = ('title', 'url')
admin.site.register(ListJob, HostListJob)
admin.site.register(python, HostListJob)
admin.site.register(command, HostListJob)
admin.site.register(lastest, HostListJob)
admin.site.register(sysadmin, HostListJob)



