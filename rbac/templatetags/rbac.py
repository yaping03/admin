import re
from django.template import Library
from django.conf import settings
register = Library()



@register.inclusion_tag("basc.html")
def menu_html(req):
    menu_dict = {}
    current_url = req.path_info
    for item in req.session.get("menu"):
        active = False
        url = item['url']
        regex = "^{0}$".format(url)
        if re.match(regex, current_url):
            active = True
        if item["menu_id"] in menu_dict:
            menu_dict[item["menu_id"]]["children"].append(
                {"title": item["title"], "url": item["url"], "active": active})
        else:
            menu_dict[item["menu_id"]] = {'menu_title': item['menu_title'],
                                          "active": active,
                                          "children": [{"title": item["title"], "url": item["url"], "active": active}]}
    return {"menu_dict":menu_dict}