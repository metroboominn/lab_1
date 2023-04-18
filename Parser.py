from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    file = open('file.txt', 'w', encoding='utf-8')
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php' # передаем необходимы URL адрес
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.find('div', id='pagecontent').find_all('a')
    txt = ''
    for item in block:
        file.write(f"{item.text}\n")
        print(item.text)
parse()