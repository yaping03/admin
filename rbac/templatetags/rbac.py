import re
from django.template import Library
from django.conf import settings
register = Library()



@register.inclusion_tag("basc.html")
def menu_html(req):
    current_url = req.path_info
    menu_list = req.session.get("menu")
    menu_dic = {}
    for item in menu_list:
        id = item["id"]
        if not item["menu_gp_id"]:
            menu_dic[id] = item
        url = item["url"]
        regex = "^{0}$".format(url)
        if re.match(regex, current_url):
            if not item["menu_gp_id"]:
                menu_dic[id]["active"] = True
            else:
                menu_dic[item["menu_gp_id"]]["active"] = True
    print(menu_dic)



    menu_dict = {}

    for item in menu_dic.values():
        active = item.get("active")
        url = item['url']
        if item["menu_id"] in menu_dict:
            menu_dict[item["menu_id"]]["children"].append(
                {"title": item["title"], "url": item["url"], "active": active})
            if active:
                menu_dict[item["menu_id"]]["active"] = True
        else:
            menu_dict[item["menu_id"]] = {'menu_title': item['menu_title'],
                                          "active": active,
                                          "children": [{"title": item["title"], "url": item["url"], "active": active}]}
    return {"menu_dict":menu_dict}