#!/usr/bin/python3.10
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime

args = sys.argv

data_hoje = datetime.now().strftime('%d_%m_%Y-%H_%M')

if len(sys.argv) != 3:
	print("Use: python3 bussola_encaminhamentos.py 'quantidade-de-paginas' 'cookie-de-sessao(laravel_session)'")
	sys.exit(1)

ultima_pagina = int(args[1]) + 1
cookie = args[2]

url ='https://app.bussolasocial.com.br/relatorios/atendimentos/encaminhamentos/realizados'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        }
vetor = []

for i in range(1,int(ultima_pagina)):
        url_pag =f'https://app.bussolasocial.com.br/relatorios/atendimentos/encaminhamentos/realizados?page={i}'
        site = requests.get(url_pag, headers=headers, cookies = {"laravel_session" : cookie})
        soup = BeautifulSoup(site.content, 'html.parser')
        try:
                tabela = soup.find(name='table')
                corpo = tabela.find(name='tbody')
                linhas = corpo.find_all(name='tr')
        except:
                print("Cookie inválido !")
                sys.exit(1)

        for linha in linhas:
                vetor.append(linha.get_text())

        print(f"Página {i}")

with open ('encaminhamentos_bussola-'+str(data_hoje)+'.csv','w',newline='', encoding='utf-8') as f:
        linha = 'Data;Nome;Destino;Status;Projeto\n'
        f.write(linha)
        for i in range(0, len(vetor)):
                row = vetor[i].split("\n")
                        
                data = row[1]
                nome = row[2]
                destino = row[3]
                status = row[4]
                projeto = row[5]
                        
                linha = data + ';' + nome + ';' + destino + ';' + status + ';' + projeto + '\n'
                f.write(linha)
	print("Finalizado !")
