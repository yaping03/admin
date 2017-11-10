from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    role = models.ManyToManyField(to="Role")

class Role(models.Model):
    name = models.CharField(max_length=16)
    permission = models.ManyToManyField(to="Permission")

class Permission(models.Model):
    title = models.CharField(max_length=16)
    url = models.CharField(max_length=64)
    code = models.CharField(max_length=16)
    is_menu = models.BooleanField()
    group = models.ForeignKey(to="Group")
    menu_gp = models.ForeignKey(to="Permission",null=True,blank=True)

class Group(models.Model):
    name = models.CharField(max_length=16)
    menu = models.ForeignKey(to="Menu")

class Menu(models.Model):
    title = models.CharField(max_length=16)