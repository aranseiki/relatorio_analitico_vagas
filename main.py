from relatorio_analitico_vagas import (iniciar_navegador, aceitar_cookies,
                            contar_elementos, encontrar_elemento, clicar_elemento, 
                            clique_mouse, extrair_texto, aguardar_elemento, 
                            voltar_pagina, salvar_csv, enviar_email_outlook, 
                            encerrar_navegador)
from time import sleep
import datetime as dt
import csv

url = 'https://cadmus.com.br/vagas-tecnologia/'

iniciar_navegador(url)

aceitar_cookies()

lista_vagas = []
lista_descricao_vagas = []

total_vagas = contar_elementos('section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div')

try:
    vaga_atual = 1
    while vaga_atual <= total_vagas:
        seletor = 'section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div:nth-child(' + str(vaga_atual) + ')'
        seletor_botao_detalhes_vaga = 'section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div:nth-child(' + str(vaga_atual) + ') > div > p.link-vagas.m-0'
        seletor_descricao_vaga = 'div#boxVaga > p'
        seletor_titulo_vaga = 'div#boxVaga > h2'
        encontrar_elemento(seletor)
        clicar_elemento(seletor)
        texto_vaga = extrair_texto(seletor)
        lista_vagas.append(texto_vaga)
        clique_mouse(encontrar_elemento(seletor_botao_detalhes_vaga))
        clicar_elemento(seletor_botao_detalhes_vaga)
        sleep(2)
        lista_descricao_vagas.append(extrair_texto(seletor_descricao_vaga))
        voltar_pagina()
        sleep(7)
        encontrar_elemento(seletor)
        vaga_atual = vaga_atual+1
except:
    ...

salvar_csv('relatorio_analitico_vagas.csv', 'w', ['nome','local','descricao'])
indice = 0
for linha in lista_vagas:
    if linha != '':
        linha = linha.split('\n') 
        nome = str(linha[0])
        local = str(linha[1])
        descricao = str(lista_descricao_vagas[indice])
        salvar_csv('relatorio_analitico_vagas.csv', 'a', [nome,local,descricao])
        indice =+1

endereco_de = 'Allan de Oliveira Almeida <techall@hotmail.com.br>'
senha = input('digite a senha: \r\n')
endereco_para = "techall@hotmail.com.br"
data_atual = dt.datetime.now().strftime('%d/%m/%Y')
assunto = 'Relatorio de vagas Cadmus - dia ' + data_atual
anexo = 'relatorio_analitico_vagas.csv'
conteudo_anexo = []
with open(anexo) as arquivo:
    arquivo_anexo = csv.reader(arquivo)
    for linha in arquivo_anexo:
        if linha != []:
            conteudo_anexo.append(linha)

mensagem = """From: {}
To: {}
Subject: {}
Content-Type: multipart/mixed; 
Content-Disposition: attachment; filename="{}"

{}

""" .format(endereco_de, endereco_para, assunto, anexo, conteudo_anexo)

enviar_email_outlook(endereco_de, senha, endereco_para, mensagem)

encerrar_navegador()
