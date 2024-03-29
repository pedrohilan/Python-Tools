#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import re

string_teste = "abracadabra alacazam ola alasosaj ala o cara"

#ex: buscando por palavra 'ala ' com espaço no final
primeiro_padrao = re.search(r'ala\s', string_teste)

#ex: buscando por palavras de 3 letras com a primeira letra dentro das especificadas
todos_padrao = re.findall(r'[ala]+\w\w', string_teste)

if todos_padrao:
    #print(primeiro_padrao.group())
    print(todos_padrao)
else:
    print("padrão não encontrado!")

#-------------------------------------------------------------------------------------------------
print("-------------------------------------------------------------------------------------------------")

string_teste_2 = "email@dom.com fulano@gmail.com first.last@gmail.com.br olamundo testandofala oi hi"

#'qualquer_letra_ou_ponto_ou_traço'@'qualquer_letra_ou_traço'.'qualquer_letra_ou_ponto'
emails = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.]+', string_teste_2)

if emails:
    print("emails :", emails)
