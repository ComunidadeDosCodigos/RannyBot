from urllib.request import *
from bs4 import BeautifulSoup
import urllib
from paylib import payloadTextoSimples,payloadReplies

#http://globoesporte.globo.com

#Variaveis Globais
dicionarioEsportes = {}

def CriarDicionario():
	#AmericaMG
	
	#AtleticoMG
	dicionarioEsportes['atletico-mg'] = "/futebol/times/atletico-mg/"
	dicionarioEsportes['atleticomg'] = "/futebol/times/atletico-mg/"
	dicionarioEsportes['galo'] = "/futebol/times/atletico-mg/"
	dicionarioEsportes['cam'] = "/futebol/times/atletico-mg/"
	
	#AtleticoParanaense
	dicionarioEsportes['atletico-pr'] = "/pr/futebol/times/atletico-pr/"
	dicionarioEsportes['furacao-pr'] = "/pr/futebol/times/atletico-pr/"
	dicionarioEsportes['furacao-paranaense'] = "/pr/futebol/times/atletico-pr/"
	dicionarioEsportes['atletico-paranaense'] = "/pr/futebol/times/atletico-pr/"
	dicionarioEsportes['atleticopr'] = "/pr/futebol/times/atletico-pr/"
	dicionarioEsportes['rubronegro-paranaense'] = "/pr/futebol/times/atletico-pr/"
	dicionarioEsportes['cap'] = "/pr/futebol/times/atletico-pr/"


	#Bahia

	#Botafogo

	#Ceara

	#Chapecoense

	#Corinthias

	#Cruzeiro

	#Flamengo
	dicionarioEsportes['flamengo'] = "/futebol/times/flamengo/"
	dicionarioEsportes['flamengo-rj'] = "/futebol/times/flamengo/"
	dicionarioEsportes['clube-de-regatas-flamengo'] = "/futebol/times/flamengo/"
	dicionarioEsportes['clube-regatas-flamengo'] = "/futebol/times/flamengo/"
	dicionarioEsportes['fla'] = "/futebol/times/flamengo/"
	dicionarioEsportes['mengão'] = "/futebol/times/flamengo/"
	dicionarioEsportes['mengo'] = "/futebol/times/flamengo/"
	dicionarioEsportes['mengao'] = "/futebol/times/flamengo/"

	#Fluminense
	dicionarioEsportes['flu'] = "/futebol/times/fluminense/"
	dicionarioEsportes['fluzao'] = "/futebol/times/fluminense/"
	dicionarioEsportes['fluzão'] = "/futebol/times/fluminense/"
	dicionarioEsportes['fluminense'] = "/futebol/times/fluminense/"
	dicionarioEsportes['fluminense-rj'] = "/futebol/times/fluminense/"

	#Gremio

	#Internacional

	#Palmeiras

	#Paraná
	dicionarioEsportes['parana'] = "/pr/futebol/times/parana-clube/"
	dicionarioEsportes['paraná'] = "/pr/futebol/times/parana-clube/"
	dicionarioEsportes['parana-clube'] = "/pr/futebol/times/parana-clube/"
	dicionarioEsportes['paraná-clube'] = "/pr/futebol/times/parana-clube/"
	dicionarioEsportes['tricolor paranaense'] = "/pr/futebol/times/parana-clube/"

	#Santos
	dicionarioEsportes['santos'] = "/sp/santos-e-regiao/futebol/times/santos/"
	dicionarioEsportes['santos-sp'] = "/sp/santos-e-regiao/futebol/times/santos/"
	dicionarioEsportes['santos-futebol-clube'] = "/sp/santos-e-regiao/futebol/times/santos/"
	dicionarioEsportes['santastico'] = "/sp/santos-e-regiao/futebol/times/santos/"
	dicionarioEsportes['peixe'] = "/sp/santos-e-regiao/futebol/times/santos/"

	#SaoPaulo

	#Sport

	#Vasco

	#Vitoria

	#F1
	dicionarioEsportes['f1'] = "/motor/formula-1/"
	dicionarioEsportes['formula1'] = "/motor/formula-1/"
	dicionarioEsportes['formula-1'] = "/motor/formula-1/"

	#volei
	dicionarioEsportes['volei'] = "/volei/"
	dicionarioEsportes['voley'] = "/volei/"

	#basquete
	dicionarioEsportes['basquete'] = "/basquete/"

def NoticiasGloboEsporte(time, linkTime):
	siteGlobo = "http://globoesporte.globo.com"
	site = siteGlobo + linkTime
	html = urlopen(site)
	bsObj = BeautifulSoup(html, "html.parser")

	bloconoticia = bsObj.findAll('p', {'class':"feed-post-body-title gui-color-primary gui-color-hover"})
	blocoresumo = bsObj.findAll('p', {'class':"feed-post-body-resumo"})
	blocolink = bsObj.findAll('a', {'class', 'feed-post-link'})
	print("Noticias: {}".format(time))
	retorno = []
	for i in range(len(blocoresumo)):
		noticia = bloconoticia[i].string
		resumo = blocoresumo[i].string
		link = blocolink[i]
		
		#Mexer aqui pra construir JSON do Carrosel 🙂 
		retorno.append("Noticia {3}: {0},{1} - PARA MAIS INFORMAÇÕES ACESSE:{2} \n".format(noticia,resumo,link['href'],i+1))

	return retorno
		
	#payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} 
	#r = requests.post(linkGrafh + token, json=payload) 

def NoticiaEsporte(sender,msg):
    CriarDicionario()
    msg = msg.split()
    if(len(msg) == 1):
        retorno = 'Para usar a função Noticias, favor seguir o seguinte modelo ex: Noticias [Esporte] / Noticias [Time]'
        listaReplies = ['Noticias Futebol', 'Noticias Volei', 'Noticias Basquete', 'Noticias F1']
        payloadReplies(sender,retorno,listaReplies)
    else:
        if(msg[1] == 'futebol'):
            retorno = 'Para usar a função Noticias Futebol, favor seguir o seguinte modelo ex: Noticias [Time]'
            listaReplies = ['Noticias AtleticoPR', 'Noticias AtleticoMG', 'Noticias Santos', 'Noticias Flamengo']
            payloadReplies(sender,retorno,listaReplies)
        if msg[1] in dicionarioEsportes:
            try:
                time = mensagem[2]
                if time in dicionarioEsportes:
                    return NoticiasGloboEsporte(time,dicionarioEsportes[time])
                else:
                    return ["Por enquanto só existem alguns times da Serie A, Aguarde para aumentarmos a cobertura ou confirme se o nome do time esta correto."]
            except:
                return NoticiasGloboEsporte(msg[1],dicionarioEsportes[msg[1]])
        else:
            return NoticiasGloboEsporte(msg[1],dicionarioEsportes[msg[1]])

def funcNoticias(sender,msg):
	retorno = NoticiaEsporte(sender,msg)
	print(retorno)
	for i in retorno:
		payloadTextoSimples(sender,i)