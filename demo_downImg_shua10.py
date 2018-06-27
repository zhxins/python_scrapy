import os
from urllib.request import urlretrieve

import requests
import time
from bs4 import BeautifulSoup
from urllib import request

# 煎蛋网 + 帅啊
def downImage():
    list_url = []
    # 页数控制，5可以随便设置
    for num in range(1, 5):
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; win64; x64) AppleWekKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = request.Request(url = url, headers = headers)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')

        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='item-img')
        # <a class="item-img" href="http://www.shuaia.net/shuaige/2018-04-24/14943.html" target="_blank"> <img alt="戴耳钉的帅哥" class="attachment-weiran" height="317" src="http://www.shuaia.net/e/data/tmp/titlepic/ddf67b85677cb9ee7cbcb0cfef776522.jpg" width="250"/> <span class="item-img-stop"></span> </a>,
        for each in targets_url:
            # print(each.span.get("class"))
            # print(each.img)
            # print(each.find("img"))
            list_url.append(each.img.get('alt') + '=' + each.get('href'))
    print(list_url)

    print("信息采集完成,共有%d张" % len(list_url))

    for each_img in list_url:

        try:
            img_info = each_img.split('=')
            target_url = img_info[1]
            filename = img_info[0] + '.jpg'
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
            }

            img_req = requests.get(url=target_url, headers=headers)

            # 如果正常返回数据做下载操作
            if  img_req.status_code == 200:
                img_req.encoding = 'utf-8'
                img_html = img_req.text
                img_bf_1 = BeautifulSoup(img_html, 'lxml')
                img_url = img_bf_1.find_all('div', class_='wr-single-content-list')
                img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
                img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
                if 'images' not in os.listdir():
                    os.makedirs('images')
                urlretrieve(url=img_url, filename='images/' + filename)
                time.sleep(1)
        except:
            print(img_bf_2)
            print('网页源码格式不正确，解析错误')
            continue

    print('下载完成！')


if __name__ == "__main__":
    downImage()
