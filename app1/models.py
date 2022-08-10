from django.db import models

# Create your models here.
class ListJob(models.Model):
    title = models.TextField(unique=True)
    link = models.TextField(unique=True)
    def __str__(self):
        return self.title


class Python(models.Model):
    title = models.TextField(unique=True)
    link = models.TextField(unique=True)
    def __str__(self):
        return self.title


class Command(models.Model):
    title = models.TextField(unique=True)
    link = models.TextField(unique=True)
    def __str__(self):
        return self.title


class Sysadmin(models.Model):
    title = models.TextField(unique=True)
    link = models.TextField(unique=True)
    def __str__(self):
        return self.title


class Lastest(models.Model):
    title = models.TextField(unique=True)
    link = models.TextField(unique=True)
    def __str__(self):
        return self.title
