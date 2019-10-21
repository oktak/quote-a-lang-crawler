import requests
from bs4 import BeautifulSoup
from dev.model.DAO import DAO
from dev.util.logger import Logger
import sys


def scrap(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
    else:
        d = DAO()
        d.write_log('crawlerError',  str(r.status_code) + ' ' + url)
        Logger().error(str(r.status_code) + ' ' + url)
        print('registered connection error!',
              str(r.status_code) + ' ' + url)
        sys.exit(1)
