import requests
import json
from paylib import payloadTextoSimples, payloadReplies

def wiki(sender,pesq):
    url = requests.get('https://pt.wikipedia.org/w/api.php?action=opensearch&search='+pesq+'=1&namespace=0&format=json')
    result = json.loads(url.text)
    a = result[1]
    b = result[2]
    c = result[3]
    lista = [a,b,c]
    if len(a) == 0:
    	retorno = "Vish, Não encontramos nada para isso."
    	payloadTextoSimples(sender, retorno)
    else:
	    for i in range(len(a)):
	    	retorno = "{}: {} \nPARA MAIS INFORMAÇÕES ACESSE:{}".format(a[i], b[i],c[i])
	    	payloadTextoSimples(sender, retorno)

def funcWiki(sender, msg):
    msg = msg.split()    
    if(len(msg) == 1):
        retorno = 'Para usar a função Wikipédia, favor seguir o seguinte modelo ex: Wikipedia Python ou Wiki Python'
        listaReplies = ['Wikipedia Python', 'Wiki Python']
        payloadReplies(sender,retorno,listaReplies)
    else:
	    pesquisar = msg[1:]
	    pesquisar = ' '.join(pesquisar)
	    wiki(sender,pesquisar)

