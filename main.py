import bs4
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
url = 'https://hh.ru/vacancies/mladshij-programmist?hhtmFromLabel=rainbow_profession&hhtmFrom=main'
headers = Headers(os="linux", headers=True).generate()
KEYWORDS = ['Python', 'Junior']
response = requests.get(url, headers=headers)
text=response.text
soup=bs4.BeautifulSoup(text, features='html.parser')
all_vacancies = soup.find_all('div', class_='vacancy-serp-item__layout')
res = []
for vacancy in all_vacancies:
    gross = vacancy.find('span', class_='bloko-header-section-3')
    name = vacancy.find('a', class_='serp-item__title')
    link = vacancy.find('a', class_='serp-item__title', href=True)['href']
    for el in KEYWORDS:
        if el in name.text:
            if gross != None:
                res.append(f'{name.text} - {gross.text} - {link}')
            else:
                res.append(f'{name.text} - Зарплата не указана - {link}')
Res = set(res)
pprint(list(Res))
