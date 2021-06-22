from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://zakup.kbtu.kz/zakupki/sposobom-zaprosa-cenovyh-predlozheniy').text

soup = BeautifulSoup(source, 'html5lib')

with open('contents.csv' , 'w+', encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['НАЗВАНИЕ', 'ДАТА', 'СТАТУС'])

    for cd_text in soup.find_all('div', class_="card-body"):
        for span in soup.select("p.card-text span"):
            for strong in soup.select("p.card-text strong"):

                tittle = cd_text.h5.a.tex
                date = strong.text
                status = span.text

                csv_writer.writerow([tittle.strip(),date,status])


csv_file.close()
