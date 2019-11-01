from bs4 import BeautifulSoup
import requests
import base64

def getDomFromUrl(url):
    req = requests.get(url)
    html = req.content #req.text
    doc = str(html, 'utf-8')
    document = BeautifulSoup(doc, features="html.parser")
    return document

def getContentFromUrl(url,type='b'):
    req = requests.get(url)
    if type == 'b':
        return req.content # 二进制
    elif type == 's':
        return req.text # 字符串
    return ''

def base64ImageFromUrl(url):
    image = getContentFromUrl(url)
    # b64encode是编码，b64decode是解码
    assert image is not None,'image not exist from url :'+url
    return str( base64.b64encode(image),'utf8')


# b64 = base64ImageFromUrl(url='https://www.lewengu.com/files/article/image/11/11098/11098s.jpg')
# print(b64)