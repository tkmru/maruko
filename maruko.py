#!/usr/bin/env python
# coding: UTF-8

from bs4 import BeautifulSoup
import hashlib
import magic
import os
import argparse
import sys

try:
    import urllib2 as ulib

except ImportError:
    import urllib.request as ulib


def display_maruko():
    print('''
　　　　　　  , - ― ‐ -  ､
　　　　　 ／　　　　　　 　 ＼
　　　　 /　　　 ∧　∧　 , 　  ヽ      ______________________________________
　　 　/　 ｌ＼:/- ∨ - ∨､!　, ',     |                                     |
　　　/ ハ.|/　　　 　 　 　 ∨|,､ﾍ   | Hi, I'm Maruko.                     |
　  |ヽ' ヽ　　　●　  　●　　　 ﾉ! l | I'm going to crawl malware from now.|
  〈｢!ヽﾊ._　　   ＿＿_　  　_.lﾉ　| |_____________________________________|
　　く´ ＼.）　   ヽ. ノ　 　（.ﾉ ￣
　　　＼　｀'ｰ-､ ＿＿_,_ - '´
　 　　 　｀ - ､ ||V V||　＼
               | ||   ||  l＼
    ''')


def fetch_soup(url):
    request = ulib.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0)')

    try:
        html = ulib.urlopen(request)

    except ulib.URLError as e:
        print('{0}, fetching {1}'.format(e.reason, url))
        return

    except Exception as e:
        print('{0}, fetching {1}'.format(e, url))
        return

    soup = BeautifulSoup(html, 'html.parser')
    return soup


def fetch_file(url, dest_path):
    try:
        file_binary = ulib.urlopen(url).read()

    except ulib.URLError as e:
        print('{0}, donwnloading from {1}'.format(e.reason, url))
        return

    except Exception as e:
        print('{0}, donwnloading from {1}'.format(e, url))
        return

    filetype = magic.from_buffer(file_binary, mime=True).decode(sys.stdin.encoding).split(' ')[0]
    file_md5 = hashlib.md5(file_binary).hexdigest()

    dest_filetype_path = dest_path + filetype
    dest_file_path = dest_filetype_path + '/' + str(file_md5)

    if not os.path.exists(dest_filetype_path):
        os.makedirs(dest_filetype_path)

    if not os.path.exists(dest_file_path):
        with open(dest_file_path, 'wb') as f:
            f.write(file_binary)

        print('-- Saved file type {0} with md5: {1}'.format(filetype, file_md5))


def parse_malwaredl(soup, dest_path):
    print('- Parcing from Malware Domain List')
    description_soup = soup('description')[1:]

    print('-- Found {0} urls'.format(len(description_soup)))

    for xml in description_soup:
        url = 'http://' + xml.string.replace('&amp;', '&').split(',')[0][6:]
        fetch_file(url, dest_path)


def parse_vxvault(soup, dest_path):
    print('- Parcing from VXVault')

    url_list = soup('pre')[0].string.replace('&amp;', '&').split('\r\n')[4:-1]
    print('-- Found {0} urls'.format(len(url_list)))

    for url in url_list:
        fetch_file(url, dest_path)


def parse_malc0de(soup, dest_path):
    print('- Parcing from Malc0de')

    description_soup = soup('description')[1:]
    print('-- Found {0} urls'.format(len(description_soup)))

    for xml in description_soup:
        host = xml.string.replace('&amp;', '&').split(',')[0][5:]
        if host is not None:
            url = 'http://' + host
            fetch_file(url, dest_path)
        else:
            ip_address = xml.text.split(',')[1][13:]
            fetch_file('http://' + ip_address, dest_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='malware crawler')
    parser.add_argument('-p', '--path', nargs=1, metavar='dest_path', help='set destination path')
    args = parser.parse_args()

    display_maruko()

    dest_path = '/opt/malware/unsorted/'

    if args.path:
        dest_path = args.path[0]

    #parse_malc0de(fetch_soup('http://malc0de.com/rss'), dest_path)
    #parse_malwaredl(fetch_soup('http://www.malwaredomainlist.com/hostslist/mdl.xml'), dest_path)
    parse_vxvault(fetch_soup('http://vxvault.siri-urz.net/URL_List.php'), dest_path)
