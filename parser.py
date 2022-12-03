#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup


def pinterest_parser(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    img = soup.find_all('img', {'class': 'hCL kVc L4E MIw'})

    print(img[0]['src'])

def main():
    parser = argparse.ArgumentParser(description  = 'Parse pinterest content url in an instant')
    parser.add_argument('-u', '--url', type = str, help = 'Pinterest URL', required = True)

    args = parser.parse_args()

    pinterest_parser(args.url)

if '__main__' == __name__:
    main()