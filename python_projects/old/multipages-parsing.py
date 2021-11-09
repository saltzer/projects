import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='pagination-pages clearfix')
    pages = divs.find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['metro'],
                         data['url']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='catalog-list')
    ads = divs.find_all('div', class_='item_table')
    for ad in ads:
        try:
            div = ad.find('div', class_='description').find('h3')
            if 'htc' not in div.text.lower():
                continue
            else:
                title = div.text.strip()
        except:
            title = ''
        try:
            div = ad.find('div', class_='description').find('h3')
            url = "https://avito.ru" + div.find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''
        try:
            div = ad.find('div', class_='data')
            metro = div.find_all('p')[-1].text.strip()
        except:
            metro = ''
        data = {'title':title,
                'price':price,
                'metro':metro,
                'url':url}
        write_csv(data)


def main():
    url = "https://avito.ru/moskva/telefony?p=1&q=htc"
    base_url = "https://avito.ru/moskva/telefony?"
    page_part = "p="
    query_par = "&q=htc"

    # total_pages = get_total_pages(get_html(url))

    for i in range(1, 3):
        url_gen = base_url + page_part + str(i) + query_par
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()