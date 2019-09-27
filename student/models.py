from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name=models.CharField(max_length=255)
    uid=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class Marks(models.Model):
    sub_name = models.CharField(max_length=255)
    total=models.IntegerField()
    internal=models.IntegerField()
    theory=models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Extras(models.Model):
    extra_curr=models.CharField(max_length=255)
    co_curr=models.CharField(max_length=255)
