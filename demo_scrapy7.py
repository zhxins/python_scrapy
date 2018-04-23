from urllib import request

from bs4 import BeautifulSoup


#  https://blog.csdn.net/c406495762/article/details/71158264
def getContent():
    download_url = "http://www.biqukan.com/1_1094/5403177.html"
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_rq = request.Request(url = download_url, headers=head)
    download_response = request.urlopen(download_rq)
    download_html = download_response.read().decode('utf-8', 'ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id='content', class_='showtxt')
    soup_text = BeautifulSoup(str(texts), 'lxml')
    # 将\xa0无法解码的字符删除
    print(soup_text.div.text.replace('\xa0', ''))


if __name__ == '__main__':
    getContent()