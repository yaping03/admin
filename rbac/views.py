from django.shortcuts import render,HttpResponse,redirect
from . import models
# Create your views here.
def test(req):
    name = "番禺"
    pwd = "123"
    obj = models.User.objects.filter(username=name,password=pwd).first()
    print(obj.roles.all().values("title").distinct())
    print(obj.roles.all().values("permissions__url").distinct())
    # for i in obj.roles.all():
    #     print(i.permissions.all().values("url","title"))

    return HttpResponse("ok")


