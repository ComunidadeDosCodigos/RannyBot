from flask import Flask, request,render_template
from flask_mqtt import Mqtt

from paylib import payloadTextoSimples,payloadAjuda, payloadReplies,testepayload

from bs4 import BeautifulSoup

import os
import traceback
import requests
import json
import urllib.request

#Funcoes
from noticias import funcNoticias
from aleatorio import funcAleatorio
from wiki import funcWiki
from piadas import funcPiada
from tratatexto import tratatexto
from games import funcGames
#Programa
app = Flask(__name__)

#Funcionalidades MQTT
app.config['MQTT_REFRESH_TIME'] = 1.0  
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'm12.cloudmqtt.com'
app.config['MQTT_BROKER_PORT'] = 16903
app.config['MQTT_USERNAME'] = 'app'
app.config['MQTT_PASSWORD'] = 'app'
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)

#Pega token.json e poe na variavel dataJson
dataJson = json.load(open('token.json'))

#Quando for fazer mudanca apenas mudar no token.json o ambiente que precisa ser modificado e o devido token :) Evitar mexer no token de producao
amb = dataJson['ambiente_ativo']
token = dataJson['ambiente'][amb]['token']
tokenVerify = dataJson['tokenVerify']
linkGrafh = dataJson['linkGrafh']

#Entradas
entrada = ['ola','oi','bom dia','ola','i aew','iae','blz', 'eae', 'e ae', 'comecar']
sentimentos = ['bom?','tudo bom?','esta bem?','como vai voce','como vai','voce esta legal','bem?']
tchau = ['ate mais','tchau','xau']
listafuncao = ['catalogo', 'funcao', 'funcoes', 'functions', 'func']
noticias = ['noticia','news','noticias']
aleatorio = ['aleatorio', 'randomico']
teste = ['teste', 'try']
ajuda = ['ajuda', 'socorro', 'help', 'socoro']
meuid = ['meuid']
wiki = ['wikipedia', 'wiki']
cryptocoin = ['crypto', 'cryptocoin', 'cryptomoeda']
games = ['jogos', 'games', 'Lançamentos do ano', 'Lançamento de Games']



@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('comunidade/#')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    s = message.payload.decode()
    json_acceptable_string = s.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    payloadTextoSimples(d['sender'],d['msg'])

def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])

#Funcoes
def funcFuncao(sender):
    lista = ['CryptoMoeda','Wiki', 'Noticias', 'Aleatorio 6', 'Socorro']
    retorno = "Tenho Somente as seguintes funções"
    payloadReplies(sender, retorno, lista)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)

            text = data['entry'][0]['messaging'][0]['message']['text'] # mensagem recebida
            #A principio nao vai precisar mais :)
            #msg = str(text.lower()) #mensagem json para string
            msg = tratatexto(str(text))

            #Variaveis
            '''
            #text = MENSAGEM QUE CHEGA PARA O FACEBOOK
            #msg = text tratado. 
            #sender = quem enviou a msg.
            '''
            sender = data['entry'][0]['messaging'][0]['sender']['id'] # id do mensageiro

            if msg in entrada: 
                retorno = 'Olá, tudo bem? Em que posso lhe ajudar, Você já conhece minhas funções? :)'#Mensagem de retorno ao usuario
                payloadTextoSimples(sender,retorno)
                funcFuncao(sender)

            elif msg in listafuncao:
                funcFuncao(sender)
               
            elif msg in sentimentos:
                retorno = 'Estou muito Bem :) Obrigado.'
                payloadTextoSimples(sender,retorno)

            elif msg in tchau:
                retorno = 'Até mais :), estou a sua disposição'
                payloadTextoSimples(sender,retorno)

            elif msg in ajuda:
            	listaAjuda = [['Policia','190'],['SAMU','192'],['Bombeiro','193']]
            	payloadAjuda(sender,listaAjuda)

            elif msg in meuid:
                payloadTextoSimples(sender,str(sender))

            elif msg in teste:
                testepayload(sender)

            else:
                #Aqui começa a parte via token:
                splitz = msg.split()
                if splitz[0] in noticias:
                    funcNoticias(sender,msg)

                elif splitz[0] in aleatorio:
                    funcAleatorio(sender,msg)

                elif splitz[0] in wiki:
                    funcWiki(sender,msg)

                elif splitz[0] in games:
                    funcGames(sender, msg)

                elif splitz[0] in cryptocoin:
                    from bitcoin import FuncCryptomoeda
                    FuncCryptomoeda(sender,msg)

                else:
                    retorno='Isso não faz parte da minha função.'
                    payloadTextoSimples(sender,retorno)
                    funcFuncao(sender)
            
        except Exception as e:
           print(traceback.format_exc())

    elif request.method == 'GET': # Para a verificação inicial
        if request.args.get('hub.verify_token') == tokenVerify:
            print("verificado")
            return request.args.get('hub.challenge')
        return render_template("home.html")
    return "Nada retornado"

if __name__ == '__main__':
    app.run(debug = True)
