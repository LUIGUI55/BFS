from arbol import Nodo

def operador_izquierdo(estado):
    nuevo_estado = estado.copy()
    nuevo_estado[0], nuevo_estado[1] = nuevo_estado[1], nuevo_estado[0]
    return nuevo_estado

def operador_central(estado):
    nuevo_estado = estado.copy()
    nuevo_estado[1], nuevo_estado[2] = nuevo_estado[2], nuevo_estado[1]
    return nuevo_estado

def operador_derecho(estado):
    nuevo_estado = estado.copy()
    nuevo_estado[2], nuevo_estado[3] = nuevo_estado[3], nuevo_estado[2]
    return nuevo_estado

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()

            hijos_datos = [
                operador_izquierdo(dato_nodo),
                operador_central(dato_nodo),
                operador_derecho(dato_nodo)
            ]
            
            for un_hijo in hijos_datos:
                hijo = Nodo(un_hijo, padre=nodo) 
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
    return None

if __name__ == "__main__":

    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    
    print(f"Buscando solucion para ir de {estado_inicial} a {solucion}...")
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    # Mostrar resultado
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None: 
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print("Ruta encontrada:")
        for paso in resultado:
            print(paso)
    else:
        print("No se encontró solución.")
