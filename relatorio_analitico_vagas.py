import csv
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = ''

def iniciar_navegador(url):
    global navegador
    navegador = Firefox()
    navegador.get(url)
    

def voltar_pagina():
    global navegador
    navegador.back()

def aguardar_elemento(seletor, tempo = 30):
    wait = WebDriverWait(navegador, tempo)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, seletor)))
    
def aceitar_cookies():
    try:
        seletor = 'div.cookieconsent'
        aguardar_elemento(seletor)
        notificacao_cookies = navegador.find_element(By.CSS_SELECTOR, seletor)
        botao_aceitar = notificacao_cookies.find_element(By.CSS_SELECTOR, 'button#aceitar')
        botao_aceitar.click()
    except:
        ...

def encontrar_elemento(seletor):
    navegador.find_element(By.CSS_SELECTOR, seletor)

def contar_elementos(seletor):
    elementos = navegador.find_elements(By.CSS_SELECTOR, seletor)
    return elementos.__len__()

def extrair_texto(seletor):
    elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
    texto_elemento = elemento.text
    return texto_elemento

def clicar_elemento(seletor):
    try: 
        elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
        elemento.click()
    except:
        ...    

def salvar_csv(arquivo, modo, conteudo):
    with open(arquivo, modo) as arquivo_manipulado:
        escreva = csv.writer(arquivo_manipulado)
        escreva.writerow(conteudo)

def encerrar_navegador():
    navegador.close()
