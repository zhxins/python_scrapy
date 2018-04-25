import random
from http import cookiejar
from urllib import request, parse

import requests


"""
url + headers
"""
def method1():
    url = 'http://www.shuaia.net/index.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; win64; x64) AppleWekKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')


"""
url + headers + timeout
"""
def method2():
    url = 'http://www.shuaia.net/index.html'
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(80, 180))
    rep = requests.get(url, headers=header, timeout=timeout)
    rep.encoding = 'utf-8'
    rep.text


"""
url + data
"""
def method3():
    url = 'http://fanyi.youdao.com/translate?' \
          'smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }

    form_data = {}
    form_data['i'] = '推送'
    form_data['from'] = 'AUTO'
    form_data['to'] = 'AUTO'
    form_data['smartresult'] = 'dict'

    data = parse.urlencode(form_data).encode('utf-8')

    response = request.urlopen(url, data)
    # if response.status == 200:
    html = response.read().decode('utf-8')


"""
url
"""
def method4():
    url = "https://www.zhihu.com/question/22918070"
    html = request.urlopen(url).read().decode('utf-8')


"""
url + headers + data
"""
def method5():
    login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    Login_Data = {}
    Login_Data['action'] = 'user_login'
    Login_Data['redirect_url'] = 'http://www.jobbole.com/'
    Login_Data['remember_me'] = '0'         #是否一个月内自动登陆
    Login_Data['user_login'] = '********'       #改成你自己的用户名
    Login_Data['user_pass'] = '********'        #改成你自己的密码
    #使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    #创建Request对象
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    # 使用自己创建的opener的open方法
    response = opener.open(req1)
    html = response.read().decode('utf-8')


