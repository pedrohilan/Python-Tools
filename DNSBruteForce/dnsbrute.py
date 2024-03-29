#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import sys
import dns.resolver

args = sys.argv

if len(sys.argv) != 3:
	print("Use: python3 dnsbrute.py 'dominio@alvo' 'lista.txt'")
	sys.exit(1)

dominio = args[1]
lista = args[2]

try:
	arq = open(lista)
	linhas = arq.read().splitlines()
except:
	print("Lista INVÁLIDA !!!")
	sys.exit(1)

for linha in linhas:
	subdominio = linha + '.' + dominio
	try:
		respostas = dns.resolver.resolve(subdominio, 'a')
		for resultado in respostas:
			print(subdominio, resultado)
	except:
		pass
