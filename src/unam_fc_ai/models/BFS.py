"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias 
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Rubio Resendiz Marco Antonio
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
This software is for educational purposes.  
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""
from collections import deque

def bfs(grafo, inicio):
    # Conjunto para rastrear nodos visitados
    visitados = set()
    # Cola para manejar el orden de exploración (FIFO)
    cola = deque([inicio])

    # Marcamos el inicio como visitado
    visitados.add(inicio)

    print(f"Orden de exploración empezando desde {inicio}:")

    while cola:
        # Extraemos el nodo que llegó primero
        nodo_actual = cola.popleft()
        print(nodo_actual, end=" ")

        # Revisamos los vecinos del nodo actual
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                
# Representación del grafo mediante un diccionario (Lista de adyacencia)
grafo_ejemplo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Ejecución
bfs(grafo_ejemplo, 2)