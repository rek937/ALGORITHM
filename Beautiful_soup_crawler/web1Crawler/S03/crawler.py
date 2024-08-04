# -*- coding: utf-8 -*-
# DELL : 192.168.5.9:7897
# HORNOR : 1270.0.0.1:7897
# Description: Simply use the requests lib

import requests
from bs4 import BeautifulSoup
import logging 
import os
import time
import random
from colorama import init, Fore
import csv

init(autoreset=True)

ip_addr = "192.168.5.9:7897"
os.environ["HTTP_PROXY"] = ip_addr
os.environ["HTTPS_PROXY"] = ip_addr

project_path = "./Beautiful_soup_crawler/web1Crawler/S03"
file_name = "S01"

sources_dir = f"{project_path}/Sources"
if not os.path.exists(sources_dir): os.mkdir(sources_dir)
source_file = os.path.join(sources_dir, f"{file_name}.csv")
with open(source_file, 'w', encoding='utf8') as f:
    f.write("ip;mac;name;type;manufacturer;ports;status")

log_dir = f"{project_path}/Log"
if not os.path.exists(log_dir): os.mkdir(log_dir)
log_file = os.path.join(log_dir, f"{file_name}.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

url = "https://www.spiderbuf.cn/playground/iplist"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

try:
    response = requests.get(url, headers=header)
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred: {e}")
else:
    if response.status_code != 404:
        logging.info(f"Successfully accessed the website: {response.status_code}")
    else:
        logging.warning(f"An warning occurred: {Fore.RED}{response.status_code}")

table_data = response.json()
table_header = ["ip", "mac","name", "type", "manufacturer", "ports", "status"]