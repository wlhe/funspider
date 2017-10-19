#!/usr/bin/env python3

# -*- coding:UTF-8 -*-

import requests
import json
from bs4 import BeautifulSoup


def save(text, file='text.txt'):
    f = open(file, 'w')
    f.write(text)
    f.close()


def get_first():
    target = "https://unsplash.com/napi/feeds/home"
    headers = {
        'authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
    req = requests.get(url=target, headers=headers,  verify=False)
    html = json.loads(req.text)
    next_page = html['next_page']
    print(next_page)

    u0 = 'https://unsplash.com/photos/'
    u2 = '/download?force=true'
    for each in html['photos']:
        print('id:', each['id'])
        url = u0 + each['id'] + u2
        res = requests.get(url)
        name = each['id'] + '.jpg'
        with open(name, 'wb') as f:
            f.write(res.content)
            f.close

    # print(req.text)


def main():
    get_first()


if __name__ == '__main__':
    main()
