import re
import json
from bs4 import BeautifulSoup
from urllib import request, parse

if __name__ == '__main__':
    ip = 'http://www.iqiyi.com/v_19rrb2yq04.html?fc=8b62d5327a54411b#vfrm=19-9-0-1'
    get_url = 'http://www.sfsft.com/index.php?url=%s' % ip

    get_movie_url = 'http://www.sfsft.com/api.php'

    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Referer':'http://www.sfsft.com/index.php?url=%s' % ip
    }

    get_url_req = request.Request(url = get_url, headers = head)
    get_url_response = request.urlopen(get_url_req)
    get_url_html = get_url_response.read().decode('utf-8')
    bf = BeautifulSoup(get_url_html, 'lxml')

    a = str(bf.find_all('script'))
    #     [<script>window.onload=function(){location.href="http://www.36605558.com/index.php?
    #     url=http://www.iqiyi.com/v_19rrb2yq04.html?fc=8b62d5327a54411b";}</script>]
    # pattern = re.compile("href= '(.+)',", re.IGNORECASE)
    pattern2 = re.compile('url=(.+)', re.IGNORECASE)
    url = pattern2.findall(a)[0]
    url = url[:-13]
    # print(url)


    get_movie_data = {
        'up':'0',
        'url':'%s' % url,
    }
    get_movie_req = request.Request(url = get_movie_url, headers = head)
    get_movie_data = parse.urlencode(get_movie_data).encode('utf-8')
    get_movie_response = request.urlopen(get_movie_req, get_movie_data)
    get_movie_html = get_movie_response.read().decode('utf-8')
    print(get_movie_data['url'])