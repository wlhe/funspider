#!/usr/bin/env python3

# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup


def save(text, file='text.txt'):
    f = open(file, 'w')
    f.write(text)
    f.close()


def main():
    target = "http://www.biqukan.com/1_1094/5403177.html"
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt')
    t = texts[0].text.replace('\xa0' * 8, '\n\n')

    print(t)
    save(t)


if __name__ == '__main__':
    main()
