from collections import deque
import math
class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range(0)]

    def costoAccion(self, m, origen, destino):
        costo = 0
        cadena = ""
        i = j = 0
        for c in range(len(self.vertices)):
            if self.vertices[c] == origen:
                i = c
            if self.vertices[c] == destino:
                j = c
        return m[i][j]

    def imprimir_matriz(self, m, texto):
        cadena = ""

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n " + ("   -" * len(m))

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[f][c])
                else:
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += "\t" + "\\"
                    else:
                        if m[f][c] is None or math.isinf(m[f][c]):
                            cadena += "\t" + "X"
                        else:
                            cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena)

    @staticmethod
    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True

    def esta_en_vertices(self, v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self, v):
        if self.esta_en_vertices(v):
            return False
        # Si no esta contenido.
        self.vertices.append(v)

        # Redimensiono la matriz de adyacencia.
        # Para preparalarla para agregar más Aristas.
        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1)]

        # Recorro la matriz y copio su contenido dentro de la matriz más grande.
        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]

        # Igualo la matriz a la matriz más grande.
        self.matriz = matriz_aux
        return True

    def agregar_arista(self, inicio, fin, valor, dirijida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        # Si estan contenidos en la lista de vertices.
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor

        # Si la arista entrante no es dirijida.
        # Instancio una Arista en sentido contrario de Fin a Inicio.
        if not dirijida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True

def obtener_sucesores(self, v):
    pos_vertice = self.vertices.index(v)
    list_sucesores = []
    for i in range(len(self.matriz)):
        if self.matriz[pos_vertice][i] is not None:
            list_sucesores.append(self.vertices[i])
    return list_sucesores
def imprimir_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

# def llenarGraf():
#     g = Grafo()

#     g.agregar_vertices("A")
#     g.agregar_vertices("B")
#     g.agregar_vertices("C")
#     g.agregar_vertices("D")
#     g.agregar_vertices("E")
#     g.agregar_vertices("F")

#     # Dirigido.
#     g.agregar_arista("A", "B", 5, True)
#     g.agregar_arista("B", "A", 3, True)
#     # g.agregar_arista("A", "D", 4, True)
#     # g.agregar_arista("A", "E", 2, True)
#     g.agregar_arista("B", "C", 1, True)
#     g.agregar_arista("B", "E", 1, True)
#     g.agregar_arista("C", "F", 5, True)
#     g.agregar_arista("D", "C", 3, True)
#     g.agregar_arista("D", "E", 3, True)
#     g.agregar_arista("D", "F", 4, True)
#     g.agregar_arista("E", "F", 8, True)

#     # g.imprimir_matriz(g.matriz, False)
#     g.imprimir_matriz(g.matriz, True)
#     imprimir_lista(obtener_sucesores(g, "B"))
