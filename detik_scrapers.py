import requests
from bs4 import BeautifulSoup

html_datas = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})
soup = BeautifulSoup(html_datas.text, 'html.parser')

popular_news = soup.find(attrs={'class':'grid-row list-content'})
titles = popular_news.find_all(attrs={'class':'media__title'})
images = popular_news.find_all(attrs={'class':'media__image'})
media_link  = popular_news.find_all(attrs={'class':'media__link'})

for img in images:
    print(img.find('a').find('img')['src'])