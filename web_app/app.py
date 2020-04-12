import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detik-popular')
def getDetikPopular():
    html_datas = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(html_datas.text, 'html.parser')

    popular_news = soup.find(attrs={'class': 'grid-row list-content'})
    titles = popular_news.find_all(attrs={'class': 'media__title'})
    images = popular_news.find_all(attrs={'class': 'media__image'})
    media_link = popular_news.find_all(attrs={'class': 'media__link'})
    return render_template('index.html', images = images)

if __name__ == '__main__':
    app.run(debug=True)


