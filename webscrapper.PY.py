import requests
from bs4 import BeautifulSoup as Soup
import csv

source = requests.get('https://www.canadapost-postescanada.ca/cpc/en/personal/sending/letters-mail/postage-rates.page')

webpage = Soup(source.content, features="html.parser")

weight = []
price = []

# Print the entire table to see its structure
print(webpage.find('table', class_='cpc-table'))

# Assuming there's only one table on the page, we'll directly target the rows within it
for row in webpage.find('table', class_='cpc-table').find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 2:  # Ensure each row has two cells (weight and price)
        weight.append(cells[0].text.strip())
        price.append(cells[1].text.strip())

file_name = 'Durvankur.csv'

print("Weights:", weight)
print("Prices:", price)

with open(file_name, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['No.', 'Weight', 'Price($)'])

    for i in range(len(price)):
        writer.writerow([i + 1, weight[i], price[i]])
