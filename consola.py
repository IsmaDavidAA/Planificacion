import planificacion
import agente


def getAccionTomada(accion, nombre):
    posX = accion.index("x")
    accionTomada = accion[0:posX]
    accionTomada = accionTomada + nombre +accion[posX+1:len(accion)]
    return accionTomada

def imprimirAcciones(listaAcciones, agente):
    for i in range(len(listaAcciones)):
        print(str(i + 1)+ "-"+getAccionTomada(listaAcciones[i], agente.name))

def acciones():
    accionesC = ["comprar(x, Pollo)","picar(x, Cebolla)"]
    return accionesC

def llenar(g):
    accionesC = acciones()
    for i in range(len(accionesC)):
        g.agregar_vertices(accionesC[i])
    # Dirigido.
    g.agregar_arista(accionesC[0], accionesC[1], 5, True)

def descontar(agentes):
    for i in range(len(agentes)): 
        agentes[i].dec()

def escogerAgente(agentes):
    for i in range(len(agentes)):
        if not agentes[i].estadoOcupado() == "Libre":
            print(str(i + 1)+ "-"+agentes[i].name +" esta "+ agentes[i].estadoOcupado()+" por "+ str(agentes[i].ocupado)+" turnos")
        else:
            print(str(i + 1)+ "-"+agentes[i].name +" esta "+ agentes[i].estadoOcupado())

if __name__ == "__main__":
    g = planificacion.Grafo()
    agentes = [agente.Agente("Chavo"), agente.Agente("Ramon")] 
    estado = 1
    llenar(g)
    accion = "comprar(x, y)"
    while (estado != 0):
        print("0-Salir")
        listaAcciones = planificacion.obtener_sucesores(g, accion)
        print("Escoger Agente")
        algunoLibre = escogerAgente(agentes)
        print(str(len(agentes)+1)+"-Pasar turno")
        estado = int(input())
        posAg = estado-1         
        if not len(agentes)+1 == estado:
            if agentes[posAg].ocupado == 0:
                if len(listaAcciones) != 0:
                    estado
                    print("-----------------------------------------------")
                    print("Escoger una accio`n")
                    imprimirAcciones(listaAcciones, agentes[estado-1])
                    estado = int(input())
                    agentes[posAg].ocupar(g.costoAccion(g.matriz, accion, listaAcciones[estado-1]))
                    accion = listaAcciones[estado-1]
                else:
                    g.imprimir_matriz(g.matriz, True)
                    estado = 0
                    print("Se termino, el plato se preparo exitosamente")
        else:
            print("Pasando 1 turno")
            descontar(agentes)



#Agente.desc(-1)
#
# 0-Salir
# 1-EscogerAgente
# ---------------------------------------
# 1-Agente 1**********
# 2-Agente 2**********
# 3-Pasar turno
# Agente.desc(-1)^ 
# ---------------------------------------
# 1-
# n-Acciones(Agente, Cebolla) - Agente.ocupar(3)
# 
# ^