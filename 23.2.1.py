import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_user_rates(user_login):
   page_num = 1
   data = []
   user_login = '60145443'
   url = f'https://www.kinopoisk.ru/user/{user_login}/votes/'
   html_content = requests.get(url).text
   soup = BeautifulSoup(html_content, 'lxml')
   entries = soup.find_all('div', class_='item')

   for entry in entries:
      nameRus = entry.find('div', class_='nameRus')
      film_name = nameRus.find('a').text

      release_date = entry.find('div', class_='date').text
      vote = entry.find('div', class_='vote').text
      data.append({'film_name': film_name, 'release_date': release_date, 'rating': vote})
   page_num +=1
   return data
user_rates = collect_user_rates(user_login='60145443')
df = pd.DataFrame(user_rates)
df.to_excel('users_rates.xlsx')
print(df)
