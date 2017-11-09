内容回顾：
	1. Django 13中操作
		- all
		- filter
		- values
		- values_list
		- get
		- exist
		- distinct
		- first
		- count
		- order_by
		- reverse
		- exclude
		- last
		- only
		- defer
		
		面试：id不等于5
		
	2. 什么是中间件？中间件应用场景？和装饰器区别？
	
	
	3. uwsgi，wsgi什么区别？
		wsgi, web服务网关接口，协议
		
		uwsgi实现协议
		wsgiref实现协议
	4. FK
		"""
		1    n1
		2    n2
		3    n3
		"""
		
		class A:
			name = xxx
			
		
			
		"""
		1   uu1    2
		2   uu2    2
		"""
		class B:
			title = xxxx
			xx = FK()
			
		# 从B表开始查
			data = models.B.objects.filter(title=xxx,xx_id=1,xx__name='xxx')
			data = models.B.objects.filter(**{"title":xxx,"xx_id":1,"xx__name":'xxx'})
			data = models.B.objects.filter(title=xxx,xx_id=1,xx__name='xxx').values("title",'xx_id','xx__name')
			data = models.B.objects.filter(title=xxx,xx_id=1,xx__name='xxx').values_list("title",'xx_id','xx__name')
		
		
			data = models.B.objects.all()
			for item in data:
				item.tile
				item.xx.name 
			
	
		# 从A表开始查
			data = models.A.objects.all()
			for item in data:
				item.id,item.name, item.b_set.all()
				
			
			data = models.A.objects.filter() # 3条
			data = models.A.objects.filter(b__id=2)
			data = models.A.objects.filter(b__id=2).values('id','name','b__title')
			data = models.A.objects.values('id','name','b__title')
			1    n1    None
			2    n2    uu1
			2    n2    uu2
			3    n3    None
				
				
			
			
	



今日内容：权限管理（菜单，使用）
	
	
内容详细：
	1. 问题，在访问列表页面时，是否需要判断：有无添加权限，有无删除权限，有无编辑权限；
		data = {
			1: {
				'codes': ['list','add','edit','del'],
				'urls':[
					/userinfo/,
					/userinfo/add/,
					/userinfo/edit/(\d+)/,
					/userinfo/del/(\d+)/,
				]
			},
			2: {
				'codes': ['list','add','edit','del'],
				'urls':[
					/userinfo/,
					/userinfo/add/,
					/userinfo/edit/(\d+)/,
					/userinfo/del/(\d+)/,
				]
			},
			
		}
		
		# 一个url对应一个code
		# 多个URL对应一个组
		
	2. 菜单  
		
		
			
内容总结：
	1. 权限修改
		初始化：
			{
				组:{
					codes:[],
					urls:[]
				}
			}
		中间件：
			url匹配
			request.permission_code_list = codes 
			
			
		是否页面上显示功能按钮：
			- 模板中 "add" in request.permission_code_list
			- 面向对象封装
		
			def userinf(request)：
				
				request.permission_code_list
				
	2. 菜单 
		- 数据库，菜单表 
		
		- 初始化：	
			获取菜单信息+权限信息
			结构化数据
			
		- 显示多级菜单
		
		- 引入css和js
		
		
		- 模板 
		
		
		- inclusion_tag+静态文件
		
	写：
		rbac中现在有什么？
			- 中间件 
			- 初始化 
			- templatestags
			- static
			- models 
		settings中：
			# ######################### rbac ############################
			PERMISSION_URL_DICT_KEY = "permission_url_dict"
			PERMISSION_MENU_KEY = "afsdfasdfadfsdfsdf"


			VALID_URL = [
				"/login/",
				"/admin.*"
			]
	用:
		- 创建project
		- 赋值rbac
		- 中间件 
		- 配置文件
		- 录入权限 
		
		- 登陆逻辑： init_permission方法
		- 模板中：
			load rbac 
			css
			
			{% menu_html %}
			
			js
			
			注意：rbac中static文件夹中再创建一个rbac文件夹，可以找到其中文件。