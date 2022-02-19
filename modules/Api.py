import json
from datetime import datetime
from TikTokApi import TikTokApi

with open('./cookies/cookie_1.json', 'r', encoding='utf-8') as f:
    cookie = json.load(f)
    f.close()

for line in cookie:
    if line['name'] == 's_v_web_id':
        api = TikTokApi(custom_verify_fp=line['value'])
        print('TT API LOADED.')


def get_video_link(user_id):
    user = api.user(username=user_id)
    user.as_dict 

    videos = []
    try:
        for video in user.videos():
            video.as_dict
            videos.append(video.as_dict)
    except: pass
    video = videos[0]
    id = video['id']
    time = int(video['createTime'])
    when = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    url = "https://www.tiktok.com/@{}/video/{}".format(user_id, id)
    print(f"[LOG] {when} {url}")