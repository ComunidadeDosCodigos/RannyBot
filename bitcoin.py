import urllib.request
import json 
from paylib import payloadTextoSimples, payloadReplies

num = 15
link = "https://api.coinmarketcap.com/v1/ticker/?convert=BRL&limit=" + str(num)

def cryptoLista(moeda):
	with urllib.request.urlopen(link) as url:
	    data = json.loads(url.read().decode())
	    for crypto in range(num):
	    	nome = (data[crypto]['name'])
	    	simbolo = (data[crypto]['symbol'])
	    	precodolar = (data[crypto]['price_usd'])
	    	precoreal = (data[crypto]['price_brl'])
	    	pct1h = (data[crypto]['percent_change_1h'])
	    	pct24h = (data[crypto]['percent_change_24h'])
	    	pct7d = (data[crypto]['percent_change_7d'])
	    	if(nome.lower() == moeda or simbolo.lower() == moeda):
	    		texto = ""
	    		texto = texto + "{} - {}\n".format(nome, simbolo)
	    		texto = texto + "Preço Dolar: {}\n".format(precodolar)
	    		texto = texto + "Preço Real : {}\n".format(precoreal)
	    		texto = texto + "Ultima 1h  : {}%\n".format(pct1h)
	    		texto = texto + "Ultima 24h : {}%\n".format(pct24h)
	    		texto = texto + "Ultima 7d  : {}%".format(pct7d)
	    		return texto


def FuncCryptomoeda(sender, msg):
	msg = msg.split()    
	if(len(msg) == 1):
		retorno = 'Para usar a função Cryptomoeda, favor seguir o seguinte modelo ex: Cryptomoeda Bitcoin ou Crypto BTC'
		listaReplies = ['Cryptomoeda Bitcoin', 'Crypto BTC']
		payloadReplies(sender,retorno,listaReplies)
	else:
		retorno = cryptoLista(msg[1])
		payloadTextoSimples(sender, retorno)
