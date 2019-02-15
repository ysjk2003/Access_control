import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Target URL")

args = parser.parse_args()
target = open("target.txt", 'w')
source_code = requests.get(args.url)
plain_txt = source_code.text
soup = BeautifulSoup(plain_txt, 'lxml')
for link in soup.select('a'):
    href = link.get('href')
    target.write(href+"\n")

target.close()