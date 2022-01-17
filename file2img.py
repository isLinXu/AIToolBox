# -*- coding:utf-8 -*-

"""
@ Author: LinXu
@ Contact: 17746071609@163.com
@ Date: 2021/12/9 下午3:40 
@ Software: PyCharm
@ File: file2img.py
@ Desc: 从file或file_url中获取图片
"""

import io
import os
import torch
import urllib
import datetime
from PIL import Image
from pathlib import Path

now = datetime.datetime.now()


def valid4file(f_url):
    if f_url is not "":
        flag = "file_url"
    else:
        flag = "file"

    return flag


def get4img(flag4file, u_f, temp_path):

    if flag4file == "file":
        image_bytes = u_f.read()
        img = Image.open(io.BytesIO(image_bytes))
    elif flag4file == "file_url":
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)

        url = str(Path(u_f)).replace(':/', '://')  # Pathlib turns :// -> :/
        u = Path(urllib.parse.unquote(u_f).split('?')[0]).name  # '%2F' to '/', split https://url.com/file.txt?auth
        t = now.isoformat()
        s = os.path.join(temp_path, t + u.split('.')[-1])
        if Path(s).is_file():
            print(f'Found {url} locally at {s}')  # file already exists
        else:
            print(f'Downloading {url} to {s}...')
            torch.hub.download_url_to_file(url, s)
            assert Path(s).exists() and Path(s).stat().st_size > 0, f'File download failed: {url}'  # check
        img = Image.open(s)
        os.system("rm " + s)

    return img


if __name__ == '__main__':
    file_url = "http:/oss.straituav.com/DJI_0458.jpg?versionId=" \
               "CAEQGhiBgMCWl7Xt6hciIDNiYTYwMmY3MzFkZDQ3MGRhYzMyM2ZlMjRhZDUzMDE4"
    image = get4img(flag4file="file_url", u_f=file_url, temp_path="./")
    image.show()
