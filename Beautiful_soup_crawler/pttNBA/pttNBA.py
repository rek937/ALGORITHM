import requests
from bs4 import BeautifulSoup
import logging
import os
import time
import random

PAGE_FLAG = True
SOURCE_FLAG = True

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

ip_addr = "http://127.0.0.1:7897"
# proxy = {"http" : "127.0.0.1:7889", "https" : "127.0.0.1:7889"}
os.environ["HTTP_PROXY"] = ip_addr
os.environ["HTTPS_PROXY"] = ip_addr
# proxies = {
#     "http": os.environ.get("HTTP_PROXY"),
#     "https": os.environ.get("HTTPS_PROXY")
# }

project_name = "./Beautiful_soup_crawler/pttNBA"
file_name = "pttNBA"

log_dir = f"{project_name}/Log"
if not os.path.exists(log_dir): os.mkdir(log_dir)
log_file = os.path.join(log_dir, f"{file_name}.log")

HTML_dir = f"{project_name}/HTML"
if not os.path.exists(HTML_dir): os.mkdir(HTML_dir)
HTML_file = os.path.join(HTML_dir, f"{file_name}.html")

source_dir = f"{project_name}/Source"
if not os.path.exists(source_dir): os.mkdir(source_dir)
source_file = os.path.join(source_dir, f"{file_name}.csv")

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

# The program is first executed
if SOURCE_FLAG:
    with open(source_file, "w", encoding="utf-8") as f:
            f.write("标题;热度;日期\n")

i = 6500
while PAGE_FLAG:
    i = i + 1
    url = f"https://www.ptt.cc/bbs/NBA/index{i}.html"
    print(url)
    try:
        response = requests.get(url, headers=header)
        # response = requests.get(url, headers=header, proxies=proxies)
        logging.info(f"Successfully accessed the website: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(e)
        logging.error(f"An error occurred: {e}")
    else:
        with open(HTML_file, "w", encoding="utf-8") as f:
            f.write(response.text)

    suop = BeautifulSoup(response.text, "html.parser")
    articles = suop.find_all("div", class_="r-ent")

    page_signals = suop.find_all("div", class_="btn-group btn-group-paging")
    for signal in page_signals:
        if signal.find("a", class_="btn wide disabled"):
            PAGE_FLAG = False

    articles_data = []
    # get title, popular and date of the article
    # articles_data = [ {}, {}, {}, ...]
    for article in articles:
        article_data = {}

        title = article.find("div", class_="title")
        if title and title.a:
            article_data["标题"] = title.a.text
        else:
            article_data["标题"] = "没有标题"

        popular = article.find("div", class_="nrec")
        if popular and popular.span:
            article_data["热度"] = popular.text
        else:
            article_data["热度"] = "N/A"

        date = article.find("div", class_="date")
        if date:
            article_data["日期"] = date.text
        else:
            article_data["日期"] = "N/A"

        articles_data.append(article_data)
    
    with open(source_file, "a", encoding="utf-8") as f:
        for article in articles_data:
            f.write(f"{article['标题']};{article['热度']};{article['日期']}\n")
    
    delay_time = random.uniform(0, 2)
    time.sleep(delay_time)
    


