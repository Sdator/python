'''
用于下载模型
'''

import os
import re
import json
import requests
from urllib.parse import urlparse
from html import unescape
from bs4 import BeautifulSoup

SCRIPT_VERSION = '1.0'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.25 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
    'cache-control': 'max-age=0'
}

代理 = {
    "http": "http://127.0.0.1:10000",
    "https": "http://127.0.0.1:10000",
}

# # 提交地址 不要这么明显
# 请求头 = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# # 访问网站
# r = requests.get(提交地址, params=请求数据, headers=请求头, proxies=代理)


def main():
    url = input('input url:')
    parse(url)


def parse(url):
    try:
        print('Parsing...')
        page = requests.get(url, headers=HEADERS, timeout=10, proxies=代理).text
        soup = BeautifulSoup(page, 'html.parser')

        modelId = urlparse(url).path.split('/')[2].split('-')[-1]
        data = unescape(soup.find(id='js-dom-data-prefetched-data').string)
        data = json.loads(data)
        name = validateTitle(data['/i/models/'+modelId]['name'])
        thumbnailData = data['/i/models/'+modelId]['thumbnails']['images']
        thumbnail = getBiggestImage(thumbnailData)
        osgjsUrl = data['/i/models/'+modelId]['files'][0]['osgjsUrl']
        modelFile = osgjsUrl.replace('file.osgjs.gz', 'model_file.bin.gz')
        texturesData = data['/i/models/'+modelId +
                            '/textures?optimized=1']['results']
        textures = []

        print('Model Id:', modelId)
        print('Name:', name)
        print('Thumbnail URL:', thumbnail)
        print('osgjs URL:', osgjsUrl)
        print('Model File:', modelFile)
        print('Textures:', len(texturesData))

        download(thumbnail, os.path.join(name, 'thumbnail.jpg'))
        download(osgjsUrl, os.path.join(name, 'file.osgjs'))
        download(modelFile, os.path.join(name, 'model_file.bin.gz'))

        for texture in texturesData:
            textureUrl = getBiggestImage(texture['images'])
            download(textureUrl, os.path.join(
                name, 'texture', validateTitle(texture['name'])))

    except AttributeError:
        raise
        return False


def getBiggestImage(images):
    size = 0
    for img in images:
        if img['size'] != None and img['size'] > size:
            size = img['size']
            imgUrl = img['url']
    return imgUrl


def validateTitle(title):
    pattern = r'[\\/:*?"<>|\r\n]+'
    newTitle = re.sub(pattern, "_", title)
    return newTitle


def download(url, filename):
    print('Downloading:', filename)
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if os.path.exists(filename):
            if os.path.getsize(filename) > 0:
                print('file exists.')
            else:
                with open(filename, 'wb') as file:
                    file.write(requests.get(url, headers=HEADERS,
                                            timeout=30, proxies=代理).content)
        else:
            with open(filename, 'wb') as file:
                file.write(requests.get(url, headers=HEADERS,
                                        timeout=30, proxies=代理).content)
    except Exception:
        pass


if __name__ == '__main__':
    main()
