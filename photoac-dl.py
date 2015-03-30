__author__ = 'Eshin Kunishima'
__license__ = 'MIT'

import re
import urllib.request
import urllib.parse
import math
import sys
import argparse

from bs4 import BeautifulSoup


base_url = 'http://www.photo-ac.com'
regex = re.compile('/main/detail_pop/\?p_id=(\d+)&f=(.+?)&.+')


def main():
    page = 1
    page_max = 999
    page_per_photo = 139

    parser = argparse.ArgumentParser(description='The photo urls collector for photo AC written by Python.')
    parser.add_argument('keyword', type=str)
    keyword = parser.parse_args().keyword

    while page <= page_max:
        print('{:d}/{:d}'.format(page, page_max), file=sys.stderr)

        request = urllib.request.Request(base_url + '/main/search?' + urllib.parse.urlencode(
            {
                'q': keyword,
                'pp': page_per_photo,
                'p': page
            }))
        request.add_header('User-Agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
        response = urllib.request.urlopen(request)

        soup = BeautifulSoup(response.read().decode(encoding='utf-8'), "html5lib")
        urls = [tag_a.get('href') for tag_a in soup.find_all('a', attrs={'class': 'thickbox'})]

        for url in [url for url in list(map(convert, urls)) if url]:
            print(url)

        page += 1
        page_max = math.ceil(int(soup.find(id="total").contents[1].string) / page_per_photo)


def convert(url):
    dl = None
    m = regex.match(url)

    if m:
        dl = base_url + '/dl/?p_id={:s}&sz=l&f={:s}'.format(m.group(1), m.group(2))

    return dl


if __name__ == "__main__":
    main()