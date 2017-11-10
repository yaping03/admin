
def session_handle(req,obj):
    data = obj.role.all().values("permission__id","permission__title","permission__is_menu","permission__url","permission__code","permission__menu_gp_id","permission__group__menu_id","permission__group__id","permission__group__menu__title").distinct()
    url_list = []
    menu_list = []
    permission = {}
    for item in data:
        tmp = {"permission__title":item["permission__title"],
               "permission__url":item["permission__url"],
               "id": item["permission__id"],
               "menu_id": item["permission__group__menu_id"],
               "is_menu": item["permission__is_menu"],
               "menu": item["permission__group__menu__title"],
               "group_id": item["permission__group__id"],
               "code": item["permission__code"],
               "menu_gp_id": item["permission__menu_gp_id"],
               }
        menu_list.append(tmp)
    for item in menu_list:
        if permission.get(item["group_id"]):
            permission[item["group_id"]]["codes"].append(item["code"])
            permission[item["group_id"]]["urls"].append(item["permission__url"])
        else:
            permission[item["group_id"]] = {
                "urls":[item["permission__url"]],
                "codes":[item["code"]]
            }
    # for item in menu_list:
    #     url_list.append(item["permission__url"])
    req.session["menu_list"] = menu_list
    req.session["permission"] = permission
    # req.session["url_list"] = url_list
    req.session["user"] = obj.user