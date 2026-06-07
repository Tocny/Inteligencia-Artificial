<!-- # Linear Regression Toolkit 📊
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Descripción
Este módulo proporciona herramientas robustas para el cálculo de regresiones lineales simples y estimaciones masivas. Desarrollado para la clase de Inteligencia Artificial, enfocado en código limpio, manejo de excepciones y logging profesional.

## 🚀 Características
- **Cálculo de Regresión:** Obtención de intercepto ($a$) y pendiente ($b$) mediante mínimos cuadrados.
- **Validación Automática:** Manejo de errores para dimensiones incompatibles o varianza cero.
- **Logging Integrado:** Registro de eventos para auditoría de modelos.
- **Type Hinting:** Código totalmente tipado para una mejor experiencia de desarrollo (DX).

## 🛠️ Instalación
Para usar esta biblioteca, clona el repositorio y asegúrate de tener las dependencias necesarias:

```bash
git clone [https://github.com/tu-usuario/nombre-repositorio.git](https://github.com/tu-usuario/nombre-repositorio.git)
cd nombre-repositorio
pip install -r requirements.txt

⚖️ Licencia

Este proyecto está bajo la Licencia MIT.

Consulta el archivo LICENSE para más detalles -->

# Algoritmo A*
El algoritmo A* es un algoritmo de búsqueda utilizado para encontrar el camino más corto entre dos nodos en un grafo. Combina las ventajas de la búsqueda de costo uniforme y la búsqueda voraz, utilizando una función de evaluación que considera tanto el costo acumulado desde el nodo inicial como una estimación heurística del costo restante hasta el nodo objetivo.

## Pseudocódigo del Algoritmo A*

función A*(Grafo, Inicio, Meta, Heurística):
    Crear Cola de Prioridad PQ (guarda [f(nodo), nodo])
    Crear Diccionario G_Score (guarda g(nodo))

    Insertamos en PQ [Heurística(Inicio), Inicio]
    G_Score[Inicio] = 0

    Mientras PQ no esté vacía:
        nodo_actual = Extraer el nodo con el menor f(nodo) de PQ

        Si nodo_actual es Meta:
            Terminar y reconstruir el camino

        Para cada vecino de nodo_actual con costo C:
            nuevo_g_score = G_Score[nodo_actual] + C
            SI nuevo_g_score < G_Score[vecino]:
                G_Score[vecino] = nuevo_g_score
                f_score = nuevo_g_score + Heurística(vecino)
                Insertar o actualizar [f_score, vecino] en PQ