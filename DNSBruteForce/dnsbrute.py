import sys
import dns.resolver

args = sys.argv

try:
	dominio = args[1]
	lista = args[2]

except:
	print("Faltam argumentos: 'dominio@alvo' 'lista.txt'")
	sys.exit(1)

try:
	arq = open(lista)
	linhas = arq.read().splitlines()
except:
	print("Lista inválida !!")
	sys.exit(1)

for linha in linhas:
	subdominio = linha + '.' + dominio
	try:
		respostas = dns.resolver.resolve(subdominio, 'a')
		for resultado in respostas:
			print(subdominio, resultado)
	except:
		pass
