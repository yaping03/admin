from django.db import models

class Menu(models.Model):
    """
    菜单组
    """
    title = models.CharField(max_length=32)


class Group(models.Model):
    """
    权限组
    """
    caption = models.CharField(verbose_name='组名称',max_length=16,default="")
    menu = models.ForeignKey(verbose_name='所属菜单',to='Menu',default=1)
class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题',max_length=32)
    url = models.CharField(verbose_name="含正则URL",max_length=64)
    code = models.CharField(verbose_name="代码",max_length=12)
    is_menu = models.BooleanField(verbose_name="是否是菜单")
    group = models.ForeignKey(to="Group",default=1)
    menu_group = models.ForeignKey(to="Permission",blank=True,null=True,related_name="menuxx")

    class Meta:
        verbose_name_plural = "权限表"

    def __str__(self):
        return self.title

class User(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    email = models.CharField(verbose_name='邮箱',max_length=32)

    roles = models.ManyToManyField(verbose_name='具有的所有角色',to="Role",blank=True)
    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.username

class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=32)
    permissions = models.ManyToManyField(verbose_name='具有的所有权限',to='Permission',blank=True)
    class Meta:
        verbose_name_plural = "角色表"

    def __str__(self):
        return self.title






