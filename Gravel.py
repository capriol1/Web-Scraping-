
import requests
from bs4 import BeautifulSoup


url = 'https://www.bikepointsc.com.br/catalogo/4/518/PG:0'

headers = {
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')
gravels = soup.find_all('div', class_='produtos catalogo')

for i in range(0, 4, 4):
    url = 'https://www.bikepointsc.com.br/catalogo/4/518/PG:0'
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    gravels = soup.find_all('div', class_='produto')
    for gravel in gravels:
        nome = gravel.find('a', title_='').get_text().strip()
        marca = gravel.find('a', class_='marca').get_text().strip()
        vendido = gravel.find('span', class_='CodigoProduto').get_text()
        preco = gravel.find('div', class_='preco').get_text()
        print(marca, vendido, preco)
