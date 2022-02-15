import csv
from multiprocessing.connection import wait
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


navegador = Firefox()
url = 'https://cadmus.com.br/vagas-tecnologia/'
navegador.get(url)

try:
    wait = WebDriverWait(navegador, 30)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookieconsent')))
    notificacao_cookies = navegador.find_element(By.CSS_SELECTOR, 'div.cookieconsent')
    botao_aceitar = notificacao_cookies.find_element(By.CSS_SELECTOR, 'button#aceitar')
    botao_aceitar.click()
except:
    ...

lista_vagas = navegador.find_elements(By.CSS_SELECTOR, 'section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div')

lista_consolidada_vagas = []
for item in lista_vagas:
    try: 
        item.click()
    except:
        ...
    lista_consolidada_vagas.append( item.text.split('\n') )

with open('relatorio_analitico_vagas.csv', 'w') as a:
    escreva = csv.writer(a)
    for linha in lista_consolidada_vagas:
        print(linha)
        escreva.writerow(linha)

navegador.close()
