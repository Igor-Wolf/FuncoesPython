#apenas o beautifulSoup e o requests não são capazes de realizar a consulta em um texto gerado dinâmicamente via Javascript
#em geral ele só eles só pegam o que já está no html nativo da página o selenium simula uma interação com o a página para ativar o js e poder receber o texto
#https://www.climatempo.com.br/ esse site ainda bloqueou o acesso tive que tentar outro para testar

from selenium import webdriver
from bs4 import BeautifulSoup

# Inicializar o driver do Selenium (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

# Carregar a página
driver.get("https://www.otempo.com.br/tempo/passos-mg")

# Extrair o HTML da página após o JavaScript ser renderizado
html = driver.page_source

# Fechar o driver
driver.quit()

# Criar o objeto soup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar a div com a classe "grau-principal"
temperatura_div = soup.find("div", class_="grau-principal")

# Obter o texto da div e do span dentro dela
temperatura_texto = temperatura_div.text.strip()

print(temperatura_texto)




