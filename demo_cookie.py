from http import cookiejar
from urllib import request

import chardet


def getCookie():

    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')

    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
    # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True, ignore_expires=True)


def loadCookie():
    # 设置保存cookie的文件的文件名,相对路径,也就是同级目录下
    filename = 'cookie.txt'
    # 创建MozillaCookieJar实例对象
    cookie = cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此用opener的open方法打开网页
    response = opener.open('https://www.baidu.com')
    # 打印信息
    # print(response.read())
    html = response.read().decode('utf-8')

    print(html)


if __name__ == "__main__":
    getCookie()
    loadCookie()