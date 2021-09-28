#!/usr/bin/python
#coding: utf-8

# Filename  : grafo.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/grafoPython/blob/main/grafo.py
# pep8: 100%

import os, time
import networkx						# librería para el manejo de grafos
import matplotlib.pyplot as plt 	# librería para ver visualmente el grafo

def goBack(grafoExiste, grafo):					# Pregunta si quieres volver a la función menú pasando parametro de existencia del grafo y datos del grafo
	op = input("¿Desea volver al menú? (S/n)\n  >: ").upper()
	if(op == "S"):
		menu(grafoExiste, grafo)
	else:
		os.system('cls')
		print("\n\n\n		Hasta luego. ")
		time.sleep(2)
		exit()

def menu(grafoExiste, grafo):
	op = int(input("\n¿Qué desea hacer?\n\n  [1] Crear grafo.\n  [2] Agregar elemento a mi grafo.\n  [3] Ver mi grafo.\n  [4] Buscar un elemento de mi grafo.\n  [5] Eliminar nodo.\n\n  [0] Salir.\n\n>: "))
	if(op == 1):
		Grafo = networkx.Graph() 					# Se crea el grafo 
		grafoExiste = True									# Variable booleana para comprobación de existencia del grafo
		print("	+- Grafo creado exitosamente.")	
		time.sleep(2)
		menu(grafoExiste, grafo)
	elif(op == 2):
		if(grafoExiste == True):
			listElementos = []
			c = int(input("\n¿Cuántas aristas deseas agregar al grafo?\n >: "))
			for i in range(0, c):
				qw = input("\nArista >: ")		# Se insertan los datos
				listElementos.append(qw)		# Se guardan en un array
				grafo.add_nodes = listElementos[i] 	# Se meten en el array del grafo
			print("\n +- Aristas agregadas correctamente.")
			print("\nCreación de vértices.\n")
			for w in range(0,c):
				print("Introduce con qué arista se conectará la arista ", listElementos[w],".")	
				x = input(" >: ")
				grafo.add_edge(listElementos[w], x)  # Se crea la conexión entre aristas
		else:
			print("\n[!] No se ha creado ningún grafo o no tiene elementos.\n")
			goBack(grafoExiste, grafo)
		time.sleep(2)
		menu(grafoExiste, grafo)
	elif(op == 3):
		if(grafoExiste == True):
			if(len(grafo.nodes)<= 0):
				print("\n[!] El grafo no tiene elementos que mostrar.\n")
				goBack(grafoExiste, grafo)
			else:
				print(" +- Cantidad de aristas: ", len(grafo.nodes)) 	
				print(" +- Cantidad de vértices: ", len(grafo.edges))
				print(" +- Aristas: ", grafo.nodes)
				print(" +- Vértices: ", grafo.edges)
				networkx.draw(grafo)			# Se inicializa la interfaz del grafo
				plt.show()						# Se visualiza
				goBack(grafoExiste, grafo)
		else:
			print("\n[!] No se ha creado ningún grafo o no tiene elementos.\n")
			goBack(grafoExiste, grafo)
	elif(op == 4):
		if(grafoExiste):
			if(len(grafo.nodes)<= 0):
				print("\n[!] El grafo no tiene elementos que mostrar.\n")
				goBack(grafoExiste, grafo)
			else:
				datoabuscar = input("¿Qué dato deseas buscar?\n>: ")
				if datoabuscar in grafo:
					print(grafo.edges(datoabuscar))		# Se muestran las aristas conectadas a el arista buscado
				else:
					print("\n[!] El dato no se encuentra o no existe.\n")
				goBack(grafoExiste, grafo)
		else:
			print("\n[!] No se ha creado ningún árbol o no tiene elementos.\n")
			goBack(grafoExiste, grafo)
	elif(op == 5):
		if(grafoExiste):
			if(len(grafo.nodes)<= 0):
				print("\n[!] El grafo no tiene elementos que mostrar.\n")
				goBack(grafoExiste, grafo)			
			else:
				datoaeliminar = input("¿Qué arista deseas eliminar?\n >: ")
				if datoaeliminar in grafo:
					grafo.remove_node(datoaeliminar)			# Se elimina el arista
					print(" +- La arista se ha eliminado correctamente.")
					menu(grafoExiste, grafo)
				else:
					print("\n[!] El dato no se encuentra o no existe.\n")
				goBack(grafoExiste, grafo)
		else:
			print("\n[!] No se ha creado ningún árbol o no tiene elementos.\n")
			goBack(grafoExiste, grafo)

	elif(op == 0):
		os.system('cls')
		print("\n\n\n		Hasta luego. ")
		time.sleep(2)
		exit()

def main():
	os.system('cls')
	grafoExiste = False
	print("      ======================")
	print("	╔═╗╦═╗╔═╗╔═╗╔═╗╔═╗	")
	print("	║ ╦╠╦╝╠═╣╠╣ ║ ║╚═╗")
	print("	╚═╝╩╚═╩ ╩╚  ╚═╝╚═╝")
	print("      ======================")
	grafo = networkx.Graph()
	menu(grafoExiste, grafo)
	
main()
