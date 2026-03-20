from arbol import Nodo

# Graph definition based on Mexican cities requested
conexiones = {
    'CDMX': {'MORELOS', 'HIDALGO', 'QUERETARO', 'JILOTEPEC'},
    'JILOTEPEC': {'CDMX', 'HIDALGO', 'QUERETARO'},
    'HIDALGO': {'CDMX', 'JILOTEPEC', 'SLP', 'QUERETARO', 'TAMAULIPAS'},
    'QUERETARO': {'CDMX', 'JILOTEPEC', 'HIDALGO', 'SLP', 'GDL'},
    'MORELOS': {'CDMX'},
    'SLP': {'HIDALGO', 'QUERETARO', 'ZACATECAS', 'MONTERREY', 'TAMAULIPAS'},
    'ZACATECAS': {'SLP', 'GDL', 'MONTERREY'},
    'GDL': {'QUERETARO', 'ZACATECAS'},
    'MONTERREY': {'SLP', 'ZACATECAS', 'TAMAULIPAS'},
    'TAMAULIPAS': {'SLP', 'MONTERREY', 'HIDALGO'}
}

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    # Check if solving for same node
    if estado_inicial == solucion:
        return nodoInicial

    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        dato_nodo = nodo.get_datos()
        
        if dato_nodo in conexiones:
            hijos_datos = conexiones[dato_nodo]
        else:
            hijos_datos = []
            
        for un_hijo in hijos_datos:
            hijo = Nodo(un_hijo, padre=nodo)
            
            # Verify if not visited
            # Optimize: check if already in list to avoid duplicates
            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                if un_hijo == solucion:
                    solucionado = True
                    return hijo
                nodos_frontera.append(hijo)
                
    return None

if __name__ == "__main__":
    estado_inicial = 'CDMX'
    solucion = 'MONTERREY'
    
    print(f"Buscando solucion para ir de {estado_inicial} a {solucion}...")
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None: 
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print("Ruta encontrada:")
        print(" -> ".join(resultado))
    else:
        print("No se encontró solución.")
