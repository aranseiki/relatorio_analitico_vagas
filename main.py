from relatorio_analitico_vagas import (iniciar_navegador, aceitar_cookies,
                            extrair_texto, salvar_csv, encerrar_navegador)


url = 'https://cadmus.com.br/vagas-tecnologia/'

iniciar_navegador(url)

aceitar_cookies('sim')

lista_vagas = []

lista_vagas = extrair_texto('section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > div')

salvar_csv('relatorio_analitico_vagas.csv', 'w', ['nome','local','descricao'])
numero = 1
for linha in lista_vagas:
    if linha != ['']:
        nome = str(linha[0])
        local = str(linha[1])
        descricao = str(linha[2])
        salvar_csv('relatorio_analitico_vagas.csv', 'a', [nome,local,descricao])

encerrar_navegador()
