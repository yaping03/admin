
def session_handle(req,obj):
        url_list = []
        url_dict = obj.roles.all().values("permissions__is_menu","permissions__title","permissions__url","permissions__group_id","permissions__code","permissions__group__menu_id","permissions__group__menu__title").distinct()
        user = obj.username
        data = {}
        menu_list = []
        for item in url_dict:
            if not item['permissions__is_menu']:
                continue
            tpl = {
                'menu_id': item['permissions__group__menu_id'],
                'menu_title': item['permissions__group__menu__title'],
                'title': item['permissions__title'],
                'url': item['permissions__url'],
                'active': False,
            }
            menu_list.append(tpl)
        for dic in url_dict:
            menu_id = dic["permissions__group__menu_id"]
            menu = dic["permissions__group__menu__title"]
            group_id = dic["permissions__group_id"]
            permissions__url = dic["permissions__url"]
            code = dic["permissions__code"]
            if group_id in data:
                    data[group_id]["code"].append(code)
                    data[group_id]["urls"].append(permissions__url)
            else:
                data[group_id]={"menu_id":menu_id,"menu":menu,"code":[code],"urls":[permissions__url]}
        # print(data)

        for url in url_dict:
            url_list.append(url["permissions__url"])
        req.session["url_list"] = url_list
        req.session["data"] = data
        req.session["menu"] = menu_list
        req.session["user"] = user
