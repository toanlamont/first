from django.db import models

# Create your models here.
class ListJob(models.Model):
    title = models.TextField(unique=True)
    url = models.TextField(unique=True)
    def __str__(self) -> str:
        return self.title


class python(models.Model):
    title = models.TextField(unique=True)
    url = models.TextField(unique=True)
    def __str__(self) -> str:
        return self.title

class command(models.Model):
    title = models.TextField(unique=True)
    url = models.TextField(unique=True)
    def __str__(self) -> str:
        return self.title

class lastest(models.Model):
    title = models.TextField(unique=True)
    url = models.TextField(unique=True)
    def __str__(self) -> str:
        return self.title

class sysadmin(models.Model):
    title = models.TextField(unique=True)
    url = models.TextField(unique=True)
    def __str__(self) -> str:
        return self.title



