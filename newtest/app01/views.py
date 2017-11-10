from django.shortcuts import render,redirect,HttpResponse

from rbac import models
from rbac.rbac.permission import session_handle
# Create your views here.
def login(req):
    if req.method=="POST":
        user = req.POST.get("user")
        pwd = req.POST.get("pwd")
        obj = models.User.objects.filter(user=user,pwd=pwd).first()
        if obj:
            session_handle(req,obj)
            return redirect("/userinfo")
    return render(req,"login.html")

class Permission:
    def __init__(self,code):
        self.code = code
    def has_add(self):
        if "add" in self.code:
            return True
    def has_edit(self):
        if "edit" in self.code:
            return True
    def has_del(self):
        if "del" in self.code:
            return True
def userinfo(req):
    permission = req.user_permission
    perm = Permission(permission)

    user_data = [
        ("xxxxx","123123"),
        ("xxxxx1","123123"),
        ("xxxxx2","123123"),
        ("xxxxx3","123123"),
        ("xxxxx4","123123"),
        ("xxxxx5","123123"),
    ]

    return render(req,"userinfo.html",{"perm":perm,"data":user_data})

def user_add(req):
    return render(req,"userinfoadd.html")
def order(req):
    return render(req,"order.html")
def order_add(req):
    return render(req,"orderadd.html")
