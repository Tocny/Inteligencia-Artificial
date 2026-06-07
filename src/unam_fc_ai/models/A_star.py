"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias 
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Escobar González Isaac Giovani
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
This software is for educational purposes.  
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""

import heapq

def a_estrella(grafo, heuristica, inicio, meta):
    
    """
    Algoritmo A* para encontrar el camino más corto entre dos nodos en un grafo.
    Parámetros:
    - grafo: Diccionario que representa el grafo, donde cada clave es un nodo y su valor es una lista de tuplas (vecino, costo).
    - heuristica: Diccionario que asigna a cada nodo una estimación del costo restante hasta el nodo meta.
    - inicio: Nodo de inicio.
    - meta: Nodo objetivo.
    Retorna:
    - camino: Lista de nodos que representa el camino más corto encontrado.
    - costo_total: Costo total del camino encontrado.
    Complejidad:
    - Tiempo: O(E log V), donde E es el número de aristas y V el número de nodos.
    - Espacio: O(V), debido a la cola de prioridad y el diccionario de visitados.
    """
    
    # Cola de prioridad que guarda: f(n), g(n), nodo_actual, camino
    cola_prioridad = [(heuristica[inicio], 0, inicio, [inicio])]
    visitados = {}
    
    # Empezamos la búsqueda A* con el nodo inicial
    while cola_prioridad:
        f, g, nodo, camino = heapq.heappop(cola_prioridad)
        
        if nodo == meta: 
            return camino, g
        
        if nodo not in visitados or g < visitados[nodo]:
            visitados[nodo] = g
            
            for vecino, costo in grafo.get(nodo, []):
                nuevo_g = g + costo
                nuevo_f = nuevo_g + heuristica[vecino]
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino + [vecino]))
    
    return None, float('inf')  # No se encontró un camino

# Datos: Grafo (pesos reales) y Heurísticas (estimaciones)
grafo = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}
h = {'A': 6, 'B': 4, 'C': 1, 'D': 0}

camino_optimo, costo_total = a_estrella(grafo, h, 'A', 'D')
print(f"Camino A*: {camino_optimo} | Costo Real: {costo_total}")