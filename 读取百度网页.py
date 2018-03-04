# 查询天气的小程序
# urllib2——用来发送网络请求
# json——用来解析获得的数据
# -*- coding: utf-8 -*-

from city import city
import urllib.request
import json

cityname = input ('city? :\n')
citycode = city.get(cityname)
if citycode:
    url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content = urllib.request.urlopen(url).read()
data=json.loads(content)
result=data['weatherinfo']
str_temp=('%s\n%s ~ %s') %(
    result['weather'],
    result['temp1'],
    result['temp2']
)

print (str_temp)