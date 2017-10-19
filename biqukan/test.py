#!/usr/bin/env python3

# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup


def save(text, file='text.txt'):
    f = open(file, 'w')
    f.write(text)
    f.close()


def get_first():
    target = "http://www.biqukan.com/1_1094/5403177.html"
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt')
    t = texts[0].text.replace('\xa0' * 8, '\n\n')

    print(t)
    save(t)


def get_dir():
    server = "http://www.biqukan.com"
    target = "http://www.biqukan.com/1_1094/"
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    print(div[0])
    for each in a:
        print(each.string, server + each.get('href'))


def main():
    get_dir()


if __name__ == '__main__':
    main()
