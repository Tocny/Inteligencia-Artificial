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

def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()

    # Marcamos el nodo como visitado y lo procesamos
    visitados.add(nodo)
    print(nodo, end=" ")

    # Exploramos recursivamente cada vecino
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Grafo de ejemplo
grafo_ejemplo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("Orden de exploración DFS empezando desde 2:")
dfs(grafo_ejemplo, 2)