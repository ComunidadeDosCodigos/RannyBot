#Funcoes para tratar texto
def retiravogaisiguais(t):
	anterior = ''
	lista = ''
	vogais = 'aeiou'
	for i in t:
		if i in vogais:
			if i != anterior:
				lista += i
		else:
			lista += i
		anterior = i
	return lista

def retiraacentos(t):
	from unicodedata import normalize
	return normalize('NFKD', t).encode('ASCII', 'ignore').decode('ASCII')

def tratatexto(texto):
	texto = texto.lower()
	texto = retiraacentos(texto)
	texto = retiravogaisiguais(texto)
	texto = texto.strip()
	return texto