#!/usr/bin/env python3

# -*- coding:UTF-8 -*-

import requests
import json
from contextlib import closing


class get_photos(object):

    def __init__(self, num):
        self.server = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.target = 'https://unsplash.com/napi/feeds/home'
        self.next_page = self.target
        self.headers = {
            'authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
        self.ids = []
        self.num = num

    def get_ids(self):
        n = 0
        while n < self.num:
            req = requests.get(url=self.next_page,
                               headers=self.headers, verify=False)
            html = json.loads(req.text)
            self.next_page = html['next_page']
            for each in html['photos']:
                self.ids.append(each['id'])
                n = len(self.ids)
                if n >= self.num:
                    break
        return n

    def download(self, id, filename):
        target = self.server.replace('xxx', id)
        req = requests.get(url=target, stream=True,
                           headers=self.headers,  verify=False)
        with closing(req) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
                        f.flush()


def main():
    total = 3
    gp = get_photos(total)
    print('Photo connecting...')
    n = gp.get_ids()
    print('get %d photo' % n)
    for i in range(len(gp.ids)):
        print('Downloading photo %d ...' % i)
        gp.download(gp.ids[i], i)


if __name__ == '__main__':
    main()
