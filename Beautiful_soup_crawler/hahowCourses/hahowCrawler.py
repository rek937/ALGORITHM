# -*- coding: utf-8 -*-
# _*_ logging: GB2312 _*_
# DELL : 192.168.5.9:7897
# HORNOR : 1270.0.0.1:7897

import requests
from bs4 import BeautifulSoup
import logging 
import os
import time
import random
from colorama import init, Fore

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

ip_addr = "192.168.5.9:7897"
os.environ["HTTP_PROXY"] = ip_addr
os.environ["HTTPS_PROXY"] = ip_addr

init(autoreset=True)

project_path = "./Beautiful_soup_crawler/hahowCourses"
file_name = "hahowCourses"

sources_dir = f"{project_path}/Sources"
os.mkdir(sources_dir) if not os.path.exists(sources_dir) else None
source_file = os.path.join(sources_dir, f"{file_name}.csv")
with open(source_file, "w", encoding="utf-8") as f:
    f.write("Title;AverageRating;SoldTickets;Price\n")

log_dir = f"{project_path}/Log"
os.mkdir(log_dir) if not os.path.exists(log_dir) else None
log_file = os.path.join(log_dir, f"{file_name}.log")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

url = "https://api.hahow.in/api/products/search?category=COURSE&limit=24&page=0&sort=TRENDING"

try:
    response = requests.get(url, headers=header)
except requests.exceptions.RequestException as e:
    logging.error(f"An error occurred: {e}")
else:
    if response.status_code != 404:
        logging.info(f"Successfully accessed the website: {response.status_code}")

    else:
        logging.error(f"An error occurred: {Fore.RED}{response.status_code}")

data = response.json()
products = data["data"]["courseData"]["products"]

course_info = [
    {
        "title" : product["title"], 
        "averageRating" : product["averageRating"], 
        "numSoldTickets" : product["numSoldTickets"], 
        "price" : product["purchasePlan"]["price"]
    }
    for product in products
]

with open(source_file, "a", encoding="utf-8") as f:
    for course in course_info:
        f.write(f"{course['title']};{course['averageRating']};{course['numSoldTickets']};{course['price']}\n")




