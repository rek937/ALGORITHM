# -*- coding: utf-8 -*-
# DELL : 192.168.5.9:7897
# HORNOR : 1270.0.0.1:7897
import requests
from bs4 import BeautifulSoup
import logging 
import os
import time
import random

url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
cookie = {"over18" : "1"}

ip_addr = "192.168.5.9:7897"
os.environ["HTTP_PROXY"] = ip_addr
os.environ["HTTPS_PROXY"] = ip_addr

project_path = "./Beautiful_soup_crawler/pttImage"
file_name = "pttImage"

sources_dir = f"{project_path}/Sources"
if not os.path.exists(sources_dir): os.mkdir(sources_dir)

log_dir = f"{project_path}/Log"
if not os.path.exists(log_dir): os.mkdir(log_dir)
log_file = os.path.join(log_dir, f"{file_name}.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

try:
    response = requests.get(url, headers=header, cookies=cookie)
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred: {e}")
else:
    logging.info(f"Successfully accessed the website: {response.status_code}")
    
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find_all("span", class_="article-meta-value")[2].text
picture_dir = f"{sources_dir}/{title}"
if not os.path.exists(picture_dir): os.mkdir(picture_dir)

links = soup.find_all("img")

picture_links = []
for link in links:
    picture_link = link.get("src")
    if picture_link:
        picture_links.append(picture_link)

exts = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]

for i, picture_link in enumerate(picture_links):

    print(f"Downloading the {i+1} picture...")
    picture_response = requests.get(picture_link, headers=header)

    for ext in exts:
        if ext in picture_link:
            picture_path = f"{picture_dir}/img_{i+1}.{ext}"
    
    with open(picture_path, "wb") as f:
        f.write(picture_response.content)
    
    delay = random.uniform(0.2, 1)
    time.sleep(delay)


    



