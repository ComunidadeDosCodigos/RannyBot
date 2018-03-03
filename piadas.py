import requests
from bs4 import BeautifulSoup
from random import randint,choice
from paylib import payloadTextoSimples

def raspaPiada(link):
	html = requests.get('https://www.piadas.com.br' + link).text
	bsObj = BeautifulSoup(html, "html.parser")

	blocopiada = bsObj.find('div', {'class':"field-item even"})
	blocop = bsObj.findAll('p')
	texto = ""
	for p in blocop[:-2]:
		texto = texto + p.string + "\n"
	return texto


def raspalink(pageNum):
	link = 'https://www.piadas.com.br/?page=' + str(pageNum)
	html = requests.get(link).text
	bsObj = BeautifulSoup(html, "html.parser")

	blocopiada = bsObj.findAll('div', {'class':"field-item even"})
	blocoahref = bsObj.findAll('a')
	lista = []
	for p in blocoahref:
		count = p['href'].count('/')
		if count == 3:
			splitz = (p['href']).split('/')
			if splitz[1] == "piadas":
				if p['href'] not in lista:
					lista.append(p['href'])
	return lista

def funcPiada(sender):
	pageNum = randint(1,40)
	lista = raspalink(str(pageNum))
	link = choice(lista)
	retorno = raspaPiada(link)
	payloadTextoSimples(sender,retorno)