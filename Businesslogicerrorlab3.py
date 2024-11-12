import requests
import sys
import urllib3
from bs4 import BeautifulSoup

import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies= {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}



def delete_carlos_user(s, url):
    

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <url>" %sys.argv[0])
        print("Example: %s www.example.com" %sys.argv[0])
        sys.exit(-1)

    s= requests.Session()
    url= sys.argv[1]
    delete_carlos_user(s, url)



if __name__ == "__main__":
    main()