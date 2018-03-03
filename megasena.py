def funcMegasena(sender):
    #Feita por Alison Aguiar
    #Em 15/12/2017
    #Em 01/02/2018 Caio Carnelos percebeu que nao estava funcionando
    source = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/').text
    soup = BeautifulSoup(source,'lxml')
    #class numbers mega-sena
    numeros = soup.find('ul',class_='numbers mega-sena')

    
    #tratamento de string
    for i in range(0,12,2):
        numeros = soup.find('ul',class_='numbers mega-sena')
        num += '-'+numeros.text[i:i+2]

    result = num[14:31]
    concurso = soup.find('div',class_='title-bar clearfix')
    resConc = concurso.h2.span.text

    retorno = 'O resultado do ultimo \n' + resConc + ' \nfoi: ' + result + ' \n\nSaiba mais aqui. \nhttp://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/\n'
    payloadTextoSimples(sender,retorno)