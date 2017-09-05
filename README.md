### ytb_jump_dl

Download youtube video or playlist with subtitle.

#### My environments

* OS X EI Capitan 10.11.6
* python 3.4.3
* requests[socks] 2.12.0
* [parsel 1.2.0](https://github.com/scrapy/parsel)
* [tqdm 4.15.0](https://github.com/tqdm/tqdm)

**note:** about Requests package above, you can install with leatest version if you can visit google directly. I used leatest version with socks error when I added proxies in requests.get(). So, I need to modify(hack) some code in Requests.

#### Modify(hack) Requests source code

1. add unicode_is_ascii(u_string) function in [this](https://github.com/requests/requests/blob/master/requests/_internal_utils.py) to your corresponding file.
2. add _get_idna_encoded_host(host) function in [this](https://github.com/requests/requests/blob/master/requests/models.py#L337) to your corresponding file.
3. use lines 388-394 in [this](https://github.com/requests/requests/blob/master/requests/models.py) replace your corresponding file's code on 379-382. And add `from ._internal_utils import unicode_is_ascii` to this file.

All above points refer to Requests leatest version.

### Man page

```bash
Usage: ytb_jump_dl path url
Args: path -> video and subtitle saved path, default: /tmp
Args: url  -> url of video or playlist
```

### Run

```bash
$ python ytb_jump_dl /Users/xxx/Downloads https://www.youtube.com...
```