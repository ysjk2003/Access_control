import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Target URL")

target = open("target.txt", 'w')
source_code = requests.get(args.url)
plain_txt = source_code.text
for link in soup.select('a'):
    href = args.url + link.get('href')
    target.write(href)