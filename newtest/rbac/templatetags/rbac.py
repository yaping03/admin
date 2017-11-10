import re
from django.template import Library
from django.conf import settings
register = Library()

@register.inclusion_tag("basc.html")
def menu_html(req):
    menu_list = req.session.get("menu_list")
    result = {}
    now_url = req.path_info
    menu_dict = {}
    for item in menu_list:
        if not item["menu_gp_id"]:
            menu_dict[item["id"]] = item
        url = item["permission__url"]
        regex = "^{0}$".format(url)
        if re.match(regex,now_url):
            if not item["menu_gp_id"]:
                menu_dict[item["id"]]["active"] = True
            else:
                menu_dict[item["menu_gp_id"]]["active"] = True
    for item in menu_dict.values():
        active = item.get("active")
        if item["menu_id"] not in result:
            result[item['menu_id']] = {
                "menu": item["menu"],
                "active": active,
                "children": [{
                    "title": item["permission__title"],
                    "url": item["permission__url"],
                    "active": active
                }]
            }
        else:
            result[item['menu_id']]["children"].append({
                "title": item["permission__title"],
                "url": item["permission__url"],
                "active": active
            })
            if active:
                result[item['menu_id']]["active"] = True
    for i in result.values():
        print(i)
    return {"result":result}