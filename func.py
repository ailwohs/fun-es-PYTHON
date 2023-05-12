from random import randint
from datetime import datetime

x=[]
total=0

#CORRIGIDO MAIUSCULA E MINUSCULA 
#CORRIGIDO VOGAIS 

def imprime_data_hora():
    from datetime import datetime;
    dhagora = datetime.now();
    datatexto = dhagora.strftime("%d/%m/%Y às %H:%M:%S");
    print(datatexto)

def gerar_array(y):
	for i in range(y):
		x.append(randint(1,1500))
	
	return(x)
	
def soma_array():
	global total
	for i in range(len(x)):
		p=x[i]
		total=total+p
		
	return(total)
		
'''def media_array(g):
    	media=total/g
	
    return(media)'''
	
def inverte_array():
	im= len(x) -1
	array=[]
	while im>=0:
		array.append(x[im])
		im=im-1
	return(array)
	########CORRIGIDO 
def converte_array(a):
    global txtArray
    txtArray = []
    txtLower = a.lower()
    for i in range(len(txtLower)):
        txtArray.append(txtLower[i])
    print (txtArray)
	
def valores_array(a):
    
    #contar vogais, consoantes CORRIGIDO 
    vogais=['a','e','i','o','u']
    consoantes=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    contVogais = 0
    contConsoantes = 0
    
    for i in range(len(a)):
        for j in range(len(vogais)):
            if (a[i]==vogais[j]):
                contVogais+=1
        for k in range(len(consoantes)):
            if (a[i]==consoantes[k]):
                contConsoantes+=1
    
    
    #CONTAR NÚMEROS CORRIGIDO
    
    num=['0','1','2','3','4','5','6','7','8','9']
    contNum = 0
    
    for i in range(len(a)):
        for j in range(len(num)):
            if (a[i]==num[j]):
                contNum+=1
    
    #CONTAR caractere ESPECIAIS CORRIGIDO
    contEspecial = (len(a) - (contVogais+contConsoantes+contNum))
    
    #print Qtd de tudo. CORRIGIDO
    print ('O texto possui', contVogais, 'vogal(is),', contConsoantes, 'consoante(s),', contNum, 'numero(s), e', contEspecial, 'caractere(s) especial(s).')
    
          #####ANTIGO= ERRADOOOO
'''def converter_array(c):
	array=[]
	cont=0
	contc=0
	contnum=0
	contesp=0
	for i in range(0, len(c)):
		array.append(c[i])
		if c[i]=='a' or c[i]=='e' or c[i]=='i' or c[i]=='o' or c[i]=='u':
			cont+=1
			
		else:
			contc+=1
		
		if c[i]=='0' or c[i]=='1' or c[i]=='2' or c[i]=='3' or c[i]=='4' or c[i]=='5' or c[i]=='6' or c[i]== '7' or c[i]=='8' or c[i]=='9':
			contnum+=1
			
		if c[i]=='!' or c[i]=='@' or c[i]=='#' or c[i]=='$' or c[i]=='%' or c[i]=='&' or c[i]=='*' or c[i]=='(' or c[i]==')' or c[i]=='?' or c[i]=='+' or c[i]==',' or c[i]=='.' or c[i]=='=' or c[i]==' ':
			contesp+=1
	
	print('esse é o seu array: ' , array)
	print("a quantidade de vogais do seu array é : ", cont)
	print("a quantidade de consoantes no seu array é de: ", contc)
	print("a quantidade de números no seu array é de: ", contnum)
	print('a quantidade de caractéres especiais no seu array é de: ', contesp)'''
	
	#########CORREÇÃO
def imprime_maiuscula(a):
    txtUpper = a.upper()
    print (txtUpper)
    
def imprime_minuscula(a):
    txtLower = a.lower()
    print (txtLower)
	
def alterna_caixa(alt):
	alt=alt
	for i in range(len(alt)):
		print(alt[i])
	
	###ERRADO
'''def imprime_maiuscula(T):
	T=T
	return(T.upper())

def imprime_minuscula(t):
	t=t
	return(t.lower())'''
	

def dia_semana(data_txt):
    from datetime import datetime;
    dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo']
    dataconvertida = datetime.strptime(data_txt, "%d/%m/%Y")
    return(dias[dataconvertida.weekday()])