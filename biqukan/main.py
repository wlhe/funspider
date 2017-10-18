#!/usr/bin/env python3

# -*- coding:UTF-8 -*-

import requests
import sys
import os
from bs4 import BeautifulSoup


class downloader(object):

    def __init__(self, server, target):
        self.server = server
        self.target = target
        self.names = []
        self.urls = []
        self.nums = 0

    def get_urls(self):
        req = requests.get(self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[15:])  # filter not need
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    def writer(self, path, name, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


def main():
    server = "http://www.biqukan.com"
    target = "http://www.biqukan.com/43_43326/"
    dl = downloader(server, target)
    dl.get_urls()
    path = "寂灭永恒.txt"
    print(path + " download start:")
    for i in range(dl.nums):
        name = dl.names[i]
        target = dl.urls[i]
        text = dl.get_contents(target)
        dl.writer(path, name, text)
        os.system("clear")
        sys.stdout.write(path + " download: %.3f%%" %
                         float(i / dl.nums) + '\n')
        sys.stdout.flush()
    print(path + "download complete!")

if __name__ == '__main__':
    main()
