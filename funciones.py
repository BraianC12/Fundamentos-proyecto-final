import csv

def guardar_lista():
	lista_inicial=[]
	with open('ranking.csv', newline='') as lista:
		reader = csv.reader(lista, delimiter=";")
		for row in reader:
			lista=[row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4])]
			lista_inicial.append(lista)
		return lista_inicial
	


#funcion que realice una tarea
#Encuentra los nombre de los equipos no descensendidos 
def clubes_sin_descensos(lista):
	for equipo in lista:
		if equipo[4]==0:
			nombre=equipo[0]
			print(nombre)
			
#retornar valores
#Suma la cantidad total de copas internacionales de todos los equipos
def titulos_internacionales(lista):
	cantidad=0
	suma=0
	for equipo in lista:
		if equipo[3]>0:
			suma=suma+equipo[3]
	return suma
	
#RETORNAR LISTAS
#muestra las listas de los equipos que nunca ganaron un titulo
def equipos_sin_titulos(lista):
	nueva_lista=[]
	for equipo in lista:
		if equipo[2]==0:
			nueva_lista.append(equipo)
	return nueva_lista


#VALOR BOOLEANO
# Muestra si el equipo ingresado existe
def consulta(lista, nombre):
	encontrado=False
	i=0
	while i<len(lista):
		if lista[i][0]==nombre:
			encontrado=True
		i=i+1
	return encontrado
	
#Retornar el elemento que sea máximo o mínimo para algún valor 
#muestra el nombre del equipo con mas puntos en la historia
def equipo_mayor_puntos(lista):
	mayor=lista[0]
	for equipo in lista:
		if equipo[1]>mayor[1]:
			mayor=equipo
	nombre=mayor[0]
	return nombre
			

#Promedio de algun valor
#promedio de todos los titulos de los primeros 50 equipos
def promedio_titulos_totales(lista):
	cantidad=len(lista)
	suma=0
	for equipo in lista:
		if equipo[2]>=0:
			suma=suma+equipo[2]#suma todos los numeros de la columna de "titulos"
	promedio=suma/cantidad
	return promedio 

#Datos ingresados por teclado
def datos_ingresados(lista):
	
	print("El programa se termina cuando el usuario ingrese 'ZZZ'")
	nombre=input("Ingrese el nombre del equipo: ")
	while nombre.upper() != "ZZZ":
		puntos=int(input("Ingrese la cantidad de puntos: "))
		titulos=int(input("Ingrese la cantidad de titulos totales: "))
		internacionales=int(input("Ingrese la cantidad de titulos internacionales: "))
		descensos=int(input("Ingrese la cantidad de descensos: "))
		equipo=[nombre, puntos, titulos, internacionales, descensos]
		lista.append(equipo)
		nombre=input("Ingrese el nombre del equipo: ")
	return lista

#Eliminar un dato de la lista
def posicion_equipo(lista, nom):
	posicion=lista[0]
	for i in lista:
		if i[0]==nom:
			cantidad=len(i)
			lista.remove(i)
	return lista

