# coding:utf-8
import requests
from parsel import Selector
from utils import gen_encode_url


def subtitle(ytb_url='', file_path=''):
    domain = 'http://downsub.com/'
    s_url = gen_encode_url(ytb_url, domain)
    print(s_url)
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080',
    }
    res = requests.get(s_url, proxies=proxies, timeout=3)
    selector = Selector(text=res.text)
    abs_url = selector.xpath(
        "//div[@id='show']/b[1]/a/@href"
    ).extract()[0]
    download_url = domain + abs_url[2:]
    title = selector.xpath(
        "//span[@class='media-heading']/text()"
    ).extract()[0]
    print(download_url)
    res = requests.get(download_url, proxies=proxies, timeout=3)
    with open('{}/{}.srt'.format(file_path, title), 'w') as srt:
        srt.write(res.text)
    pass


if __name__ == '__main__':
    # 待下载ytb的url
    url = 'https://www.youtube.com/watch?v=Ttw816mwnQY'
    filepath = '/Users/zhangyue/Downloads'
    subtitle(url, filepath)
