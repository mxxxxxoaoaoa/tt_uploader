import json
from os import listdir
from os.path import isfile, join
import os
import random
import shutil


def get_videos():
    return listdir("./upload")


def get_video(video):
    response = []
    try:
        onlyfiles = [f for f in listdir(f"./upload/{video}") if isfile(join(f"./upload/{video}", f))]
        if 'caption.txt' in onlyfiles and 'tags.txt' in onlyfiles and 'video.mp4' in onlyfiles:
            response.append({
                'cap': open(f"./upload/{video}/caption.txt").read(),
                'tag': open(f"./upload/{video}/tags.txt").read(),
                'vid': os.path.abspath(f"./upload/{video}/video.mp4")
            })
            print(f"{video} - GOOD.")
            return response
        else: 
            print(f'{video} - BAD.')
            shutil.rmtree(f'./upload/{video}')
    except: os.remove(f"./upload/{video}")

def randomly_video():
    dirs = listdir("./upload")
    return get_video(random.choice(dirs))


for video in get_videos():
    get_video(video)
