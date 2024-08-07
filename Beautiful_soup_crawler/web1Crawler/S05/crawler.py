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

init(autoreset=True)

# Local proxy (need change)
ip_addr = "127.0.0.1:7897"
os.environ["HTTP_PROXY"] = ip_addr
os.environ["HTTPS_PROXY"] = ip_addr

# file name (need change)
file_name = "S05"
# project path (or change)
project_path = f"./Beautiful_soup_crawler/web1Crawler/{file_name}"

resources_dir = f"{project_path}/Resources"
if not os.path.exists(resources_dir): os.mkdir(resources_dir)
# Create resource file base on requirement 


log_dir = f"{project_path}/Log"
if not os.path.exists(log_dir): os.mkdir(log_dir)
log_file = os.path.join(log_dir, f"{file_name}.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

login_url = "https://www.spiderbuf.cn/playground/e02"
target_url = "https://www.spiderbuf.cn/playground/e02/list"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
          "Cookie": "admin=cc49f9e4f12fda966ef3b2b8a7ca5bfd"}
payload = {"username" : "admin", "password" : "123456"}
session = requests.Session()

try:
    login_response = requests.post(login_url, headers=header, data=payload)
    target_response = session.get(target_url, headers=header)
    logging.info("New test begin !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred: {e}")
else:
    if target_response.status_code != 404:
        logging.info(f"Successfully accessed the website: {target_response.status_code}")
    else:
        logging.warning(f"An warning occurred: {Fore.RED}{target_response.status_code}")

target_response.encoding = "utf-8"
soup = BeautifulSoup(target_response.text, "html.parser")
table_td = soup.find("table").find_all("td")
table_data = [td.text for td in table_td]

table_header = ["排名", "企业估值(亿元)", "企业信息", "CEO", "行业"]

table = [
    dict(zip(table_header, table_data[i : i + len(table_header)])) for i in range(0, len(table_data), len(table_header))
]

resource_file = os.path.join(resources_dir, f"{file_name}.csv")
with open(resource_file, 'w', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=table_header)
    writer.writeheader()
    writer.writerows(table)
    print(f"Data has been saved in {resource_file}")