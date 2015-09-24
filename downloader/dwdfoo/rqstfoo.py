__author__ = 'Ashton'

import urllib.request as ureq
import urllib.error as uerr


def check_connection():
    try:
        response = ureq.urlopen('https://www.google.com', timeout=1)
        return True
    except uerr as err:
        pass
    return False


def wall_get(owner_id, offset='0', count='15'):
    return 'https://api.vk.com/method/wall.get?owner_id=' + \
           owner_id + '&offset=' + offset + '&count=' + count


def wall_get_by_id(post_id):
    return 'https://api.vk.com/method/wall.getById?posts=' + post_id + \
           '&extended=1&copy_history_depth=2'