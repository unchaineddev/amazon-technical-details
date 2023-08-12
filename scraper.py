import requests
from bs4 import BeautifulSoup
import lxml
import re

HEADERS = {   
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
}

URL = input("Enter a URL: ")
webpage = requests.get(URL, headers=HEADERS)
# print(webpage)


soup = BeautifulSoup(webpage.content, "lxml")


# Fetches the title
def title():
    title = soup.find("span", attrs={"id":'productTitle'})
    # title = title.string.split('|')[0].strip().split('1920 x 1080')[0]
    title = title.string
    print(title)

# Create a dictionary to store the extracted details


def technical_specs():
    tech_details = {}
    rows = soup.find_all("tr")
    # Loop through each row
    for row in rows:
        th = row.find("th", class_="a-color-secondary")
        td = row.find("td", class_="a-size-base prodDetAttrValue")
        if th and td:
            key = th.get_text(strip=True)
            value = td.get_text(strip=True)
            tech_details[key] = value

    # Print the extracted technical details
    for key, value in tech_details.items():
        print(f"{key}: {value}")
        if key == 'ASIN':
            break

    

print()
title()
print()
technical_specs()
