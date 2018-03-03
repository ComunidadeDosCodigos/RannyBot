from random import randint
from paylib import payloadTextoSimples

def geraAleatorio(qtd,minimo=1,maximo=60):
    lista = []
    while(len(lista)<=qtd):
        x = randint(minimo,maximo)
        if x not in lista:
            lista.append(x)
    return lista

def funcAleatorio(sender,msg):
    msg = msg.split()
    if(len(msg) == 1):
        retorno = 'Para usar a função Aleatorio, favor seguir o seguinte modelo ex: Aleatorio [Quantidade de Números] [Minimo] [Maximo]'
        payloadTextoSimples(sender,retorno)
    else:
        try:
            qtd = int(mensagem[1])
        except SyntaxError:
            retorno = "Para usar essa função se deve passar 3 Argumentos, Quantidade de Numeros, o Valor *Minimo e o *Maximo"
            payloadTextoSimples(sender, retorno)
            retorno = "Exemplo: Aleatorio 6 1 60 \n Aleatorio 6, Consideramos o valor minimo e maximo default como 1-60"
            payloadTextoSimples(sender, retorno)
            return 0
        try:
            minimo = int(mensagem[2])
        except IndexError:
            minimo = 1

        try:
            maximo = int(mensagem[3])
        except IndexError:
            maximo = 60

        if qtd > (maximo - minimo):
            retorno = "Valores Invalidos"
            payloadTextoSimples(sender,retorno)
        else:
            lista = geraAleatorio(qtd,minimo,maximo)
            lista.sort()
            texto = str(lista[0])
            for i in lista[1:]:
                texto = texto + "-" + str(i)
            retorno = "Os {} Números sorteados entre {}-{} foram: \n".format(qtd,minimo,maximo) + texto
            payloadTextoSimples(sender, retorno)