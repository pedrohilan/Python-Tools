#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import whois, sys

if len(sys.argv) == 2:
	dominio = sys.argv[1]
else:
	print("Use python3 whoisss.py 'dominio.com'")
	sys.exit(1)

try:
	print(whois.whois(dominio))
except Exception as e:
	print(e)
