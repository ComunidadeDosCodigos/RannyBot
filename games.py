#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from paylib import payloadTextoSimples, payloadReplies

def games(sender):

    pagina = requests.get("https://www.comparegames.com.br/lancamentos-janeiro-2018--ps4").text
    bs4Parser = BeautifulSoup(pagina, "html.parser")

    busca_tags = bs4Parser.find_all('p', {'class':'nm'})
    busca_link = bs4Parser.find_all('a', {'class':'gm'})

    print("LISTA DE JOGOS LANÇAMENTOS DE 2018\n")
    for item in busca_tags:
        retorno = "{}".format(item.get_text())

def funcGames(msg, sender):
    msg = msg.split()    
    if(len(msg) == 1):
        retorno = 'Para usar a função Games, favor seguir o seguinte modelo ex:'
        listaReplies = ['Games', 'Lançamentos']
        payloadReplies(sender,retorno,listaReplies)
    else:
	    print('None')
