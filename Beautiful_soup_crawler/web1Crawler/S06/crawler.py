# -*- coding: utf-8 -*-
# DELL : 192.168.5.9:7897
# HORNOR : 127.0.0.1:7897
# Description: login with CAPTCHA use AI to recognize CAPTCHA
import requests
from bs4 import BeautifulSoup
import logging 
import os
import time
import random
from colorama import init, Fore
import csv
import base64

init(autoreset=True)

# Local proxy (need change)
ip_addr = "127.0.0.1:7897"
os.environ["HTTP_PROXY"] = ip_addr
os.environ["HTTPS_PROXY"] = ip_addr

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://www.spiderbuf.cn/playground/n02"

response = requests.get(url, headers=header)

response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

picture = soup.find("img", class_="img-responsive center-block").get("src")

picture = picture.replace("data:image/png;base64,", "")

picture = base64.b64decode(picture)


# file name (need change)
file_name = "S06"
# project path (or change)
project_path = f"./Beautiful_soup_crawler/web1Crawler/{file_name}"
resources_dir = f"{project_path}/Resources"
if not os.path.exists(resources_dir): os.mkdir(resources_dir)
# Create resource file base on requirement 
source_file = os.path.join(resources_dir, f"{file_name}.jpg")
with open(source_file, 'wb') as f:
    f.write(picture)