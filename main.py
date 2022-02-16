from relatorio_analitico_vagas import (iniciar_navegador, aceitar_cookies,
                            contar_elementos, encontrar_elemento, clicar_elemento, 
                            extrair_texto, aguardar_elemento, voltar_pagina, salvar_csv, encerrar_navegador)
from time import sleep

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
        clicar_elemento(seletor_botao_detalhes_vaga) 
        sleep(2)
        aguardar_elemento(seletor_titulo_vaga)
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

encerrar_navegador()
