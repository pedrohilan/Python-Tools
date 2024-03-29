#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import requests
import sys
import json

def fazer_requisicao(cep):
    query = "https://viacep.com.br/ws/" + cep + "/json/"

    try:
        req = requests.get(query)
        # transformando a resposta JSON em um dicionario com a biblioteca 'json'
        dicionario = json.loads(req.text)
        print("\nCidade: " +dicionario['localidade'])
        print("UF: " +dicionario['uf'])
        print("Logradouro: "+dicionario['logradouro'])
        print("Bairro: "+dicionario['bairro']+"\n")
    except:
        print("\nCEP não encontrado!\n")


sair = False
while not sair:
    op = input("Digite um CEP(somente números) ou 's' para sair : ")

    if op == "s":
        sair = True
    else:
        fazer_requisicao(op)
