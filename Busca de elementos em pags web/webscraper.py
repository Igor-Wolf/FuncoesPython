from bs4 import BeautifulSoup
import requests

# objeto site recebendo todo o conteudo da requisição http do site...
site = requests.get("https://www.climatempo.com.br/").content
# objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

#transforma o html em string e o print vai exibir o html
#print(soup.prettify())
soup.prettify()


temperatura = soup.find("h2", class_="-bold -font-18 -gray-dark-2 _center _margin-b-10")
print(temperatura.text)


temperatura = soup.find("span", id="current-weather-city")
print(temperatura)

print(soup.title.string)
print(soup.a)
print(soup.p.string)




# <h2 class="-bold -font-18 -gray-dark-2 _center _margin-b-10">
# Tempo agora em <br>
# <span id="current-weather-city" class="-text">São Paulo, SP</span></h2>
