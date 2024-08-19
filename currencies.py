import requests
import csv

url = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"
response = requests.get(url)
data = response.json()

with open('currencies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['currency', 'code', 'bid', 'ask'])
    for rate in data[0]['rates']:
        writer.writerow([rate['currency'], rate['code'], rate['bid'], rate['ask']])