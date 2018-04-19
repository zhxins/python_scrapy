# *_* coding:utf-8 *_*
import json
from urllib import request, parse

import chardet


def youdao_tanslate():

    try:
        url = 'http://fanyi.youdao.com/translate?' \
              'smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

        # 创建字典
        # form_data = {'type': 'AUTO', 'i': 'directory', 'doctype': 'json', 'xmlVersion': '1.8', 'keyfrom': 'fanyi,web',
        #              'ue': 'ue:UTF-8', 'action': 'FY_BY_CLICKBUTION'}
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }

        form_data = {}
        form_data['i'] = '美丽'
        form_data['from'] = 'AUTO'
        form_data['to'] = 'AUTO'
        form_data['smartresult'] = 'dict'
        form_data['client'] = 'fanyideskweb'
        form_data['salt'] = '1524126419105'
        form_data['sign'] = '30eeb69607ccae43fc5a5699867e2a6f'
        form_data['doctype'] = 'json'
        form_data['version'] = '2.1'
        form_data['keyfrom'] = 'fanyi.web'
        form_data['action'] = 'FY_BY_REALTIME'
        form_data['typoResult'] = 'false'

        data = parse.urlencode(form_data).encode('utf-8')

        response = request.urlopen(url, data)
        if response.status == 200:
            html = response.read().decode('utf-8')

            # 转换成json串
            translate_results = json.loads(html)
            translate_results = translate_results['translateResult'][0][0]['tgt']

            print("%s 翻译后的结果是 %s" % (form_data['i'], translate_results))

    except:
        print("error")


def get_csdn():

    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    # 写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    # 创建Request对象
    req = request.Request(url, headers=head)
    # 传入创建好的Request对象
    response = request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息
    print(html)


def proxy():

    # 访问网址
    url = 'http://www.whatismyip.com.tw/'
    # 这是代理IP
    proxy = {'http': '223.241.78.133:18118'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # 安装OPener
    request.install_opener(opener)
    # 使用自己安装好的Opener
    response = request.urlopen(url)
    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    # 打印信息
    print(html)


def test():
    pass



if __name__ == "__main__":

    # youdao_tanslate()
    # get_csdn()
    proxy()
