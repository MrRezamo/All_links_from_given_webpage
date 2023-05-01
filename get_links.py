import requests as rq
from bs4 import BeautifulSoup
import re


def check_website_address():
    url_pattern = re.compile(r"^(https?://)?(www\.)?[a-z0-9\-]+(\.[a-z]{2,})(/[a-z0-9\-._~:/?#[\]@!$&'()*+,;=]*)?$")
    while True:
        url = input("Enter a website address: ")
        if url_pattern.match(url):
            try:
                response = rq.get("https://"+url)
                return response
            except rq.exceptions.ConnectionError as e:
                print(f"Error fetching URL:{e}")
        else:
            print("Invalid URL. Please enter a valid website address.")


def get_link(response):
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    with open("myLinks.txt", 'a') as saved:
        print(links[:10], file=saved)
    return links[:10]


get_link(check_website_address())