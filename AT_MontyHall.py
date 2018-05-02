import numpy as np
from random import shuffle

#Creacion de la puerta
def sort_doors():
	lista = ['goat','goat','car']
	np.random.shuffle (lista)
	return lista

#Escogencia de la puerta
def choose_door():
	num = [0,1,2]
	numero = np.random.choice(num,1)[0]
	return numero

#Se revela una sola puerta
def reveal_door(lista,choice):
	i = 0
	for i in range(len(lista)):
		if i != choice:
			if lista[i] == 'goat':
				lista [i] = 'GOAT_MONTY'
				return lista		
			
#Se revelan todas las puertas
def finish_game(lista,choice,change):
	if (change == False):
		return lista[choice]
	else:
		for i in range(3):
			if (lista[i] != 'GOAT_MONTY') and (i != choice):
				return lista[i]


#Simulacion del juego
for i in range (100):
	choose = choose_door()
	a = 0
	b = 0
	if ('car' == finish_game(reveal_door(sort_doors(),choose),choose,True)):
		a = a+1
		print a
	if ('car' == finish_game(reveal_door(sort_doors(),choose),choose,False)):
		b = b+1
print 'Cambiando de puerta la probabilidad de ganar es' , a/100.0
print 'Sin cambiar de puerta la probabilidad de ganar es' , b/100.0
	
