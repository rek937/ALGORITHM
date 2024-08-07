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

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
          "referer" : "https://cqut.cqbys.com/jobfair",
          "cookie" : "_pk_id.1955.559d=d850722eb30a529e.1722680988.; PHPSESSID2=vlhfmluljvpji3j23k80l70o97; _pk_ses.1955.559d=1"}
url = "https://cqut.cqbys.com/campus"

response = requests.get(url, headers=header)

response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

announcement_label = soup.find("li", class_="span7")

print(announcement_label.text)
