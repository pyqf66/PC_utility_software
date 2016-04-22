# -*- coding:utf-8 -*-
from common.util.HttpUrlConnection import HttpUrlConnection
from common.util.logger import console
import random

rand_num = random.random()
console.debug(rand_num)
cookie_url="http://www.kuaidi100.com/all/jd.shtml?from=openv"
url = 'http://www.kuaidi100.com/query?type=jd&postid=17309087617&id=1&valicode=&temp='+str(rand_num)
request_object = HttpUrlConnection(url=url,get_cookie_url=cookie_url,get_cookie_method="GET")
result = request_object.request_with_cookies().json()["data"]
for i in result:
    console.debug(i)

