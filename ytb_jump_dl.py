# coding:utf-8
import sys
from requests import Session
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
from utils import ytb_download, get_urls_in_playlist


def run(url, file_path):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/60.0.3112.90 Safari/537.36',
        'connection': 'keep-alive',
    }
    proxies = {
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080',
    }
    session = Session()
    session.headers = headers
    session.proxies = proxies

    # pool = ThreadPool(4)
    #
    # fun = partial(ytb_download, session, file_path)
    if 'playlist' in url:
        # pool.map(fun, get_urls_in_playlist(session, url))
        for video_url in get_urls_in_playlist(session, url):
            ytb_download(session, file_path, video_url)
    else:
        # url_iter = []
        # url_iter.append(url)
        # pool.map(fun, url_iter)
        ytb_download(session, url, file_path)
    # pool.close()
    # pool.join()

if __name__ == '__main__':
    args_len = len(sys.argv)
    if args_len == 1 or args_len > 3 \
            or 'youtube' not in sys.argv[args_len-1]:
        print('Usage: ytb_jump_dl path url')
        print('Args: path -> video and subtitle saved path, default: /tmp')
        print('Args: url  -> url of video or playlist')
        print('Ex: ytb_jump_dl /Users/xxx/Downloads http://www.youtube.com...')
        exit(1)
    if args_len == 2:
        file_path = '/tmp'
    else:
        if sys.argv[1][-1] == '/':
            file_path = sys.argv[1][:-1]
        else:
            file_path = sys.argv[1]
    url = sys.argv[2]
    run(url, file_path)
    print('Done')

