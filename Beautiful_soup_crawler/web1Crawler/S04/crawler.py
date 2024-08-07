# -*- coding: utf-8 -*-
# DELL : 192.168.5.9:7897
# HORNOR : 127.0.0.1:7897
# Description: HTTP POST request data scraping

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
file_name = "S04"
# project path (or change)
project_path = f"./Beautiful_soup_crawler/web1Crawler/{file_name}"

resources_dir = f"{project_path}/Resources"
if not os.path.exists(resources_dir): os.mkdir(resources_dir)
# Create resource file base on requirement 
source_file = os.path.join(resources_dir, f"{file_name}.csv")
with open(source_file, 'w', encoding='utf8') as f:
    f.write("Serial Number;IP Address;MAC Address;Device Name;Device Type;Operating System;Open Ports;Online Status")


log_dir = f"{project_path}/Log"
if not os.path.exists(log_dir): os.mkdir(log_dir)
log_file = os.path.join(log_dir, f"{file_name}.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")


url = "https://www.spiderbuf.cn/playground/s08"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
payload = {"level" : 8}

try:
    response = requests.post(url, headers=header, data=payload)
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred: {e}")
else:
    if response.status_code != 404:
        logging.info(f"Successfully accessed the website: {response.status_code}")
    else:
        logging.warning(f"An warning occurred: {Fore.RED}{response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table")
table_data = table.find_all("td") # type: ignore
table_data = [table_data.text for table_data in table_data]
table_header = ["Serial Number", "IP Address", "MAC Address", "Device Name", "Device Type", "Operating System", "Open Ports", "Online Status"]
data = [
    dict(zip(table_header, table_data[i : i + len(table_header)])) for i in range(0, len(table_data), len(table_header))
]

with open(source_file, 'w', encoding="utf8") as f:
    writer = csv.DictWriter(f, fieldnames=table_header)
    writer.writeheader()
    writer.writerows(data)
    logging.info("Data written to csv file")