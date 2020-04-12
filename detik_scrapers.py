import requests
from bs4 import BeautifulSoup

html_datas = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})
print(html_datas.text)