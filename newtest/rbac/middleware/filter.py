import re
from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response
class MyFilter(MiddlewareMixin):
    def process_request(self,req):
        now_url = req.path_info
        permission = req.session.get("permission")
        # url_list = req.session.get("url_list")
        if not permission:
            return redirect("/login")
        print(now_url)
        print(settings.ALLOW_URL)
        for url in settings.ALLOW_URL:
            regex = "^{0}$".format(url)
            if re.match(regex,now_url):
                return None
        flag = False
        for item in permission.values():
            for url in item["urls"]:
                regex = "^{0}$".format(url)
                if re.match(regex,now_url):
                    print(item["codes"])
                    req.user_permission = item["codes"]
                    flag = True
                    return None
        if not flag:
            return HttpResponse("不存在或无权访问")


