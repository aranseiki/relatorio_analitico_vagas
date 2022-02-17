import os
import csv
import smtplib
import ssl
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


navegador = ''


def cls():
    os.system('cls')


def criar_diretorio(caminho):
    if not os.path.exists(caminho):
        os.mkdir(caminho)


def iniciar_navegador(url):
    global navegador
    navegador = Firefox()
    navegador.get(url)
    estado_pronto = False
    aguardar_pagina_carregar(estado_pronto)


def aguardar_pagina_carregar(estado_pronto):
    while estado_pronto == False:
        estado = navegador.execute_script('return window.document.readyState')
        if estado != 'complete':
            sleep(1)
        else:
            estado_pronto = True


def voltar_pagina():
    navegador.back()
    estado_pronto = False
    aguardar_pagina_carregar(estado_pronto)


def centralizar_elemento(seletor):
    navegador.execute_script(
        'document.querySelector("' + seletor
        + '").scrollIntoView({block: "center"})'
    )


def aguardar_elemento(seletor, tempo=30):
    try:
        wait = WebDriverWait(navegador, tempo)
        sleep(0.5)
        wait.until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, seletor)
            ))
        centralizar_elemento(seletor)
    except:
        ...


def aceitar_cookies():
    try:
        seletor = 'div.cookieconsent'
        aguardar_elemento(seletor)
        centralizar_elemento(seletor)
        notificacao_cookies = navegador.find_element(By.CSS_SELECTOR, seletor)
        botao_aceitar = notificacao_cookies.find_element(
                By.CSS_SELECTOR, 'button#aceitar'
            )
        botao_aceitar.click()
        estado_pronto = False
        aguardar_pagina_carregar(estado_pronto)
    except:
        ...


def encontrar_elemento(seletor):
    navegador.find_element(By.CSS_SELECTOR, seletor)
    centralizar_elemento(seletor)


def contar_elementos(seletor):
    elementos = navegador.find_elements(By.CSS_SELECTOR, seletor)
    centralizar_elemento(seletor)
    return elementos.__len__()


def extrair_texto(seletor):
    elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
    texto_elemento = elemento.text
    centralizar_elemento(seletor)
    return texto_elemento


def clicar_elemento(seletor):
    try:
        centralizar_elemento(seletor)
        elemento = navegador.find_element(By.CSS_SELECTOR, seletor)
        elemento.click()
        estado_pronto = False
        aguardar_pagina_carregar(estado_pronto)
    except:
        ...


def clique_mouse(webelemento):
    action = ActionChains(navegador)
    action.double_click(webelemento).perform()


def salvar_csv(arquivo, modo, conteudo):
    with open(arquivo, modo, encoding='utf8') as arquivo_manipulado:
        escreva = csv.writer(arquivo_manipulado)
        escreva.writerow(conteudo)


def tratar_anexo(conteudo_anexo):
    conteudo_anexo = str(
        conteudo_anexo
    ).replace('[', '').replace('\\n', ' ')\
        .replace('"', '').replace(';', '')\
        .replace("', '", "'; '").replace(',', '')\
        .replace(';', ',').replace(']', '\r\n')
    return conteudo_anexo


def enviar_email_outlook(endereco_de, senha, endereco_para, mensagem):
    login = endereco_de.split('<')[1].replace('>', '')
    servidor = smtplib.SMTP('smtp.office365.com')
    servidor.connect("smtp.office365.com", 587)
    servidor.ehlo('hello')
    contexto = ssl.create_default_context()
    servidor.starttls(context=contexto)
    servidor.login(str(login), senha)
    servidor.sendmail(endereco_de, endereco_para, mensagem)
    servidor.quit()


def encerrar_navegador():
    navegador.close()
