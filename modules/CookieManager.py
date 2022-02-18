import json
from os import listdir
from os.path import isfile, join


def get_cookies():
    cookie_files = [f for f in listdir("cookies") if isfile(join("cookies", f))]
    cookies = []
    for cookie_file in cookie_files:
        with open('./cookies/{}'.format(cookie_file), 'r', encoding="utf-8") as f:
            cookie = json.load(f)
            f.close()
        cookies.append(cookie)
    return cookies


def correct_cookie(cookie):
    if cookie['sameSite'] != 'Strict':
        cookie['sameSite'] = 'Strict'
    return cookie