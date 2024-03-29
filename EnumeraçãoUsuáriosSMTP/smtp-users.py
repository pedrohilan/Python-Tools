#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import socket, sys

if len(sys.argv) == 4:
    server = sys.argv[1]
    port = int(sys.argv[2])
    list_users = sys.argv[3]
else:
    print("Use python3 smtp-users.py server port list_users.txt\nExemple python3 smtp-users.py 127.0.0.1 25 list.txt")
    sys.exit(1)

try:
    arq = open(list_users)
    linhas = arq.read().splitlines()
except Exception as e:
    print("exceção: ",e)
    sys.exit(1)

for user in linhas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.recv(1024)
    send_user = "VRFY " + user + "\n"
    # usando o .encode para mandar mensagem em 'bytes-like'
    s.send(send_user.encode())
    result = s.recv(1024)
    s.close()

    if "252".encode() in result:
        print("[+] *** USUÁRIO VÁLIDO *** [+] -> ", user)
    elif "550".encode() in result:
        print("[-] Usuário não encontrado [-] -> ", user)
    elif "503".encode() in result:
        print("[-] Servidor requer autenticação ! [-]")
        break
    elif "500".encode() in result:
        print("Comando VRFY não suportado pelo servidor !")
        break
    else:
        print("Resposta do servidor: ", result)
