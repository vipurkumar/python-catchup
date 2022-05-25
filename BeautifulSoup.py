from bs4 import BeautifulSoup
import requests as rq

page = rq.get('https://www.letour.fr/en/rankings/stage-1')
soup = BeautifulSoup(page.text, 'html.parser')
soup
