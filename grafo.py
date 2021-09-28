#!/usr/bin/python
#coding: utf-8

# Filename  : grafo.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/04IDMA/grafo.py
# pep8: 100%

import os, time
import networkx
import matplotlib.pyplot as plt

def goBack(grafoExiste, grafo):					# Pregunta si quieres volver a la función menú pasando parametro de existencia de árbol y datos del árbol
	op = input("¿Desea volver al menú? (S/n)\n  >: ").upper()
	if(op == "S"):
		menu(grafoExiste, grafo)
	else:
		os.system('cls')
		print("\n\n\n		Hasta luego. ")
		time.sleep(2)
		exit()

def getInfo(listElementos):
	return listElementos


def menu(grafoExiste, grafo):
	op = int(input("\n¿Qué desea hacer?\n\n  [1] Crear grafo.\n  [2] Agregar elemento a mi grafo.\n  [3] Ver mi grafo.\n  [4] Buscar un elemento de mi grafo.\n  [5] Eliminar nodo.\n\n  [0] Salir.\n\n>: "))
	if(op == 1):
		Grafo = networkx.Graph() 					# Se crea el árbol sin valores
		grafoExiste = True									# Variable booleana para comprobación de existencia de árbol
		print("	+- Grafo creado exitosamente.")	
		time.sleep(2)
		menu(grafoExiste, grafo)
	elif(op == 2):
		if(grafoExiste == True):
			listElementos = []
			c = int(input("\n¿Cuántas aristas deseas agregar al grafo?\n >: "))
			for i in range(0, c):
				qw = input("\nArista >: ")
				listElementos.append(qw)
				grafo.add_nodes = listElementos[i]
			print("\n +- Aristas agregadas correctamente.")
			print("\nCreación de vértices.\n")
			for w in range(0,c):
				print("Introduce con qué arista se conectará la arista ", listElementos[w],".")
				x = input(" >: ")
				grafo.add_edge(listElementos[w], x)
		else:
			print("\n[!] No se ha creado ningún grafo o no tiene elementos.\n")
			goBack(grafoExiste, grafo)
		time.sleep(2)
		getInfo(listElementos)
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
				networkx.draw(grafo)
				plt.show()
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
					print(grafo.edges(datoabuscar))
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
					grafo.remove_node(datoaeliminar)
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
	grafo = networkx.Graph()
	menu(grafoExiste, grafo)
	
main()

# Grafo = networkx.Graph()
# Grafo.add_node("A")      # add_node("n") agrega "n" como nodo del grafo
# Grafo.add_node("B")
# Grafo.add_node("C")
# Grafo.add_edge("A","B")  # add_edge("e") agrega "e" como borde de un nodo
# Grafo.add_edge("B","C")
# Grafo.add_edge("C","U")

# print(len(Grafo.nodes))
# print(len(Grafo.edges))
# print(Grafo.nodes)
# print(Grafo.edges)