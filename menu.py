from funciones import guardar_lista
from funciones import clubes_sin_descensos
from funciones import titulos_internacionales
from funciones import equipos_sin_titulos
from funciones import consulta
from funciones import equipo_mayor_puntos
from funciones import promedio_titulos_totales
#funciones extras
from funciones import datos_ingresados #ingreso de datos
from funciones import posicion_equipo #eliminar datos
import os #libreria para limpiar pantalla


def menu():
	print("\n1: Lista de todos los elementos")
	print("2: Los nombres de los equipos que no descendieron")
	print("3: Cantidad de titulos internacionales en total")
	print("4: Equipos sin titulos")
	print("5: Saber si esta el equipo ingresado")
	print("6: Nombre del equipo con mas puntos historicamente")
	print("7: Promedio de los titulos de los equipos a lo largo del tiempo")
	print("8: Ingreso de un nuevo equipo: ")
	print("9: Eliminar un elemento de la lista")
	print("10: Limpiar pantalla")
	print("11: Salir\n")
	
def limpiar():
	os.system("cls")


lista_equipos=guardar_lista()

menu()

opcion=input("Ingrese una opcion: ")
while opcion != "11":
	if opcion=="1":
		for i in lista_equipos:
			print(i)
	elif opcion=="2":
		print("Los clubes que nunca descendieron son: ")
		clubes_sin_descensos(lista_equipos)
	elif opcion=="3":
		titulos=titulos_internacionales(lista_equipos)
		print("La cantidad de titulos internacionales totales que hay son: " + str(titulos) + "\n")
	elif opcion=="4":
		sin_titulos=equipos_sin_titulos(lista_equipos)
		for a in sin_titulos:
			print (a)
	elif opcion=="5":
		nombre=input("Ingrese el nombre del equipo: ")
		print("¿Existe el equipo en la lista?")
		equipo=consulta(lista_equipos, nombre)
		print(equipo)
	elif opcion=="6":
		equipos_puntos=equipo_mayor_puntos(lista_equipos)
		print("El equipo con mayor cantidad de puntos es: ")
		print(equipos_puntos)		
	elif opcion=="7":
		promedio=promedio_titulos_totales(lista_equipos)
		print("El promedio de los titulos totales es: " + str(promedio) + "\n")
		
	elif opcion=="8":
		datos=datos_ingresados(lista_equipos)
		for a in datos:
			print(a)
		
	elif opcion=="9":
		equipo=input("Ingrese el nombre del equipo a eliminar: ")
		eliminar=posicion_equipo(lista_equipos, equipo)
		for b in eliminar:
			print(b)
			
	elif opcion=="10":
		limpiar()
	else:
		print ("Opcion incorrecta")
	menu()
	opcion=input("Ingrese una opcion: ")
	
#Cosas corregidas:
#1. El parametro de la lista en las fuciones
#2. La funcion menu que se repetia en todas las opciones
#3. Linea 58 del programa "funciones" sacar la variable 'nombre' del for
#4. Funcion de los booleanos
