import random

import requests


class HtmlDownLoader(object):

    def downloader(self, url):
        if url is None:
            return
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }
        timeout = random.choice(range(80, 180))
        response = requests.get(url, headers =header, timeout =timeout)
        response.encoding = 'utf-8'
        if response.status_code != 200:
            return None
        return response.text