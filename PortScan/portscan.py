#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import sys
import socket

args = sys.argv

if len(sys.argv) == 3:
	dominio = args[1]
	ports = args[2]
else:
	print("Use: python3 portscan.py host port(s)\nExample: python3 portscan '127.0.0.1' '80,443,21,22'")
	sys.exit(1)

if '.' in ports:
	print("No points !")
	sys.exit(1)
else:
	ports = ports.split(',')

verifica = 0
for port in ports:
	#especificando o tipo de conexao
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#especificando o tempo maximo para resposta
	client.settimeout(0.5)
	#conexao que retorna um codigo como resposta - connect_ex
	cod = client.connect_ex((dominio, int(port) ))
	#quando o codigo é 0 significa que a porta esta aberta
	if cod == 0:
		print("\nPORTA:", int(port), "ABERTA")
	else:
		verifica += 1

if verifica == len(ports):
	print("\nTodas as portas estão fechadas !")