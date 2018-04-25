from lxml import etree

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def cookie():
    url = 'https://www.baidu.com'
    headers = {'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               }
    s = requests.session()
    req = s.get(url=url, headers=headers)
    print(s.cookies)


def seleium():
    url = 'http://pythonscraping.com'

    # 有时运行出错，是seleium版本不对，pip install selenium==2.48.0
    driver = webdriver.PhantomJS(executable_path=r'D:\soft\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url=url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())


# 蜜罐圈套
def honey_pot():
    url = 'http://pythonscraping.com/pages/itsatrap.html'

    # 有时运行出错，是seleium版本不对，pip install selenium==2.48.0
    driver = webdriver.PhantomJS(
        executable_path=r'D:\soft\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url=url)
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        if not link.is_displayed():
            print('连接：' + link.get_attribute('href') + ',是一个蜜罐圈套')

    fields = driver.find_elements_by_tag_name('input')
    for field in fields:
        if not field.is_displayed():
            print('不要改变' + field.get_attribute('name') + '的值')


def proxy():
    page = 1
    S = requests.session()
    target_url = 'http://www.xicidaili.com/nn/%d' % page
    target_headers = {'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                      'Referer': 'http://www.xicidaili.com/nn/',
                      'Accept-Encoding': 'gzip, deflate, sdch',
                      'Accept-Language': 'zh-CN,zh;q=0.8',
                      }

    target_response = S.get(url=target_url, headers=target_headers)
    target_response.encoding = 'utf-8'
    target_html = target_response.text
    print(proxy)
    bf1_ip_list = BeautifulSoup(target_html, 'lxml')
    bf2_ip_list = BeautifulSoup(str(bf1_ip_list.find_all(id = 'ip_list')), 'lxml')
    ip_list_info = bf2_ip_list.table.contents

    proxys_list = []
    for index in range(len(proxys_list)):
        if index % 2 == 1 and index != 1:
            dom = etree.HTML(str(ip_list_info[index]))
            ip = dom.xpath('//td[2]')
            port = dom.xpath('//td[3]')
            protocol = dom.xpath('//td[6]')
            proxys_list.append(protocol[0].text.lower() + '#' + ip[0].text + '#' + protocol[0].text)
    print(proxys_list)





if __name__ == '__main__':
    # cookie()
    # seleium()
    # honey_pot()
    proxy()