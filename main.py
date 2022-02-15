from relatorio_analitico_vagas import (iniciar_navegador, aceitar_cookies,
                            contar_elementos, encontrar_elemento, clicar_elemento, 
                            extrair_texto, salvar_csv, encerrar_navegador)


url = 'https://cadmus.com.br/vagas-tecnologia/'

iniciar_navegador(url)

aceitar_cookies()

lista_vagas = []

total_vagas = contar_elementos('section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div')

vaga_atual = 1
while vaga_atual <= total_vagas:
    seletor = 'section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div:nth-child(' + str(vaga_atual) + ')'
    encontrar_elemento(seletor)
    clicar_elemento(seletor)
    texto_vaga = extrair_texto(seletor)
    lista_vagas.append(texto_vaga)
    vaga_atual = vaga_atual+1

salvar_csv('relatorio_analitico_vagas.csv', 'w', ['nome','local','descricao'])
for linha in lista_vagas:
    if linha != '':
        linha = linha.split('\n') 
        nome = str(linha[0])
        local = str(linha[1])
        descricao = str(linha[2])
        salvar_csv('relatorio_analitico_vagas.csv', 'a', [nome,local,descricao])

#encerrar_navegador()
