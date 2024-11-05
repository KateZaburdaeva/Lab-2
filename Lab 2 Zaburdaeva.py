from csv import reader
import csv
import random
import xml.dom.minidom as minidom
from csv import DictReader
import os

# Задание 1

with open('books-en.csv', 'r', encoding='windows-1251') as long:
    long = reader(long, delimiter = ';')
    count = 0
    for row in long:
        if len(row[1]) > 30:
            count += 1

print(f'Количество записей, длина которых больше 30 символов: {count}')


# Задание 2

def open_books():
    with open('books.csv', newline='', encoding='UTF 8') as fh: 
        reader = csv.reader(fh, delimiter=';', quotechar='"')
        books = [row for row in reader]
    return books[1:]

def search_author():
    author = input("Введите автора:")
    for book in books:
        if (book[4]==author or book[3]==author) and float(book[7]) < 150:
            print (book[3], book[1], f'цена: {book[7]}')

books = open_books()
search_author() 


# Задание 3

with open('books-en.csv', 'r', encoding='windows-1251') as file:
    reader = csv.reader(file, delimiter=';')
    table = list(reader)

count = len(table)

random_indices = sorted(random.sample(range(count), 20))

with open('result.txt', 'w', encoding='utf-8') as output:
    for i in random_indices:
        row = table[i]
        output.write(f'{row[2]}. {row[1]} - {row[3]}\n')


# Задание 4

xml_file = open('currency.xml', 'r', encoding='latin-1')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
books_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    value = str(child.firstChild.data)
    books_dict[name] = value

print(books_dict)

xml_file.close()


# Дополнительное задание 1

unique = set()

with open('books-en.csv', 'r', encoding='latin-1') as file:
    reader = DictReader(file, delimiter=';')
    
    for row in reader:
        publisher = row.get('Publisher')
        if publisher:
            unique.add(publisher)

for publisher in unique:
    print(publisher)


# Допоплнительное задание 2

books = {}

with open('books-en.csv', 'r', encoding='latin-1') as file:
    reader = DictReader(file, delimiter=';')
    
    for row in reader:
        title = row.get('Book-Title')
        downloads = row.get('Downloads')

        if title and downloads and downloads.isdigit():
            downloads = int(downloads)
            books[title] = downloads

top = sorted(books.items(), key=lambda x: x[1], reverse=True)[:20]

print("20 самых популярных книг:")
for title, downloads in top:
    print(f"{title}: {downloads} скачиваний")

