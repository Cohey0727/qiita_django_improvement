from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
