import datetime as dt
import csv
import relatorio_analitico_vagas as passo
from time import sleep


try:
    mensagem_erro = ''
    data_atual = dt.datetime.now().strftime('%d/%m/%Y')
    hora_atual_atual = dt.datetime.now().strftime('%H/%M/%S')
    pasta_dia_atual = data_atual.replace('/', '_')
    pasta_extracao = 'relatorio'
    pasta_log = 'log'
    nome_arquivo_csv = 'relatorio_analitico_vagas.csv'
    caminho_principal = '.\\'+'executado'
    caminho_dia_atual = (
        caminho_principal+'\\'+pasta_dia_atual
    )
    caminho_extracao = (
        caminho_principal+'\\'+pasta_dia_atual+'\\'+pasta_extracao
    )
    caminho_log = (
        caminho_principal+'\\'+pasta_dia_atual+'\\'+pasta_log
    )
    nome_log = 'log_relatorio_analitico_vagas.txt'

    passo.criar_diretorio(caminho_principal)
    passo.criar_diretorio(caminho_dia_atual)
    passo.criar_diretorio(caminho_extracao)
    passo.criar_diretorio(caminho_log)

    try:
        url = 'https://cadmus.com.br/vagas-tecnologia/'
        passo.iniciar_navegador(url)
    except:
        mensagem_erro = TypeError(
            "Erro no processo 1: Iniciar navegador"
        )
        raise mensagem_erro

    try:
        passo.aceitar_cookies()

        lista_vagas = []
        lista_descricao_vagas = []

        total_vagas = passo.contar_elementos(
            'section#solucoes-texto > div > div:nth-child(2) \
                > div > div#pfolio > div'
        )

        vaga_atual = 1
        while vaga_atual <= total_vagas:
            seletor = 'section#solucoes-texto > div > div:nth-child(2) > div > \
            div#pfolio > div:nth-child(' + str(vaga_atual) + ')'
            seletor_botao_detalhes_vaga = 'section#solucoes-texto > div > div:nth-child(2) > div > div#pfolio > \
            div:nth-child(' + str(vaga_atual) + ') > div > p.link-vagas.m-0'
            seletor_descricao_vaga = 'div#boxVaga > p'
            seletor_titulo_vaga = 'div#boxVaga > h2'
            passo.encontrar_elemento(seletor)
            passo.clicar_elemento(seletor)
            sleep(2)
            texto_vaga = passo.extrair_texto(seletor)
            lista_vagas.append(texto_vaga)
            passo.clicar_elemento(seletor_botao_detalhes_vaga)
            sleep(2)
            lista_descricao_vagas.append(
                passo.extrair_texto(seletor_descricao_vaga)
            )
            passo.voltar_pagina()
            sleep(7)
            passo.encontrar_elemento(seletor)
            vaga_atual = vaga_atual+1
    except:
        mensagem_erro = TypeError(
            "Erro no processo 2: Extração de dados do site"
        )
        raise mensagem_erro

    try:
        passo.salvar_csv(
            caminho_dia_atual + '\\' + nome_arquivo_csv, 'w', [
                'Nome da vaga', 'Local da vaga', 'descrição da vaga'
            ]
        )
        indice = 0
        for linha in lista_vagas:
            if linha != '':
                linha = linha.split('\n')
                nome = str(linha[0])
                local = str(linha[1])
                descricao = str(lista_descricao_vagas[indice])
                passo.salvar_csv(
                    caminho_extracao + '\\' + nome_arquivo_csv,
                    'a',
                    (nome, local, descricao)
                )
                indice = indice + 1
    except:
        mensagem_erro = TypeError(
            "Erro no processo 3: Salvar extração no arquivo .csv"
        )
        raise mensagem_erro

    try:
        endereco_de = 'Allan de Oliveira Almeida <techall@hotmail.com.br>'
        senha = input('digite a senha: \r\n')
        endereco_para = "techall@hotmail.com.br"
        assunto = 'Relatorio de vagas Cadmus - dia ' + data_atual
        anexo = caminho_extracao + '\\' + nome_arquivo_csv
        conteudo_anexo = []
        with open(anexo, encoding='utf8') as arquivo:
            arquivo_anexo = csv.reader(arquivo)
            for linha in arquivo_anexo:
                if linha != []:
                    conteudo_anexo.append(linha)

        conteudo_anexo = passo.tratar_anexo(conteudo_anexo)

        mensagem = """From: {}
        To: {}
        Subject: {}
        Content-Type: multipart/mixed;
        Content-Disposition: attachment; filename="{}"

        {}

        """ .format(endereco_de, endereco_para, assunto, anexo, conteudo_anexo)

        passo.enviar_email_outlook(
            endereco_de, senha, endereco_para,
            mensagem.encode('utf8', 'replace')
        )
    except:
        mensagem_erro = TypeError(
            "Erro no processo 5: Envio de e-mail com a extração em anexo"
        )
        raise mensagem_erro

    try:
        passo.encerrar_navegador()
    except:
        mensagem_erro = TypeError(
            "Erro no processo 6: Encerrar navegador"
        )
        raise mensagem_erro
except:
    status = 'NOK'
    mensagem = mensagem_erro

finally:
    if mensagem_erro == '':
        status = 'OK'
        mensagem = 'Processo concluído com sucesso'

    log = open(caminho_log + '\\' + nome_log, 'a', encoding='utf8')
    resultado = (status, mensagem, data_atual + ': ' + hora_atual_atual)
    resultado = str(
        resultado
    ).replace('(', '').replace(')', '').replace('TypeError', '')
    log.write(resultado + '\r\n')
    log.close
