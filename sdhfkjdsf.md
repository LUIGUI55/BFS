'''python

if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP', 'MEXICALI', 'CHIHUAHUA'},
        'SAPOPAN': {'ZACATECAS', 'MEXICALI'},
        'GUADALAJARA': {'CHIAPAS'},
        'CHIAPAS': {'CHIHUAHUA'},
        'MEXICALI': {'SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
        'SLP': {'CDMX', 'MEXICALI'},
        'ZACATECAS': {'SAPOPAN', 'SONORA', 'CHIHUAHUA'},
        'SONORA': {'ZACATECAS', 'MEXICALI'},
        'MICHOACAN': {'CHIHUAHUA'},
        'CHIHUAHUA': {'MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX', 'CHIAPAS'}
    }

    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)
    
    # Mostrar resultado
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None: 
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print("Ruta encontrada:", resultado)
    else:
        print("No se encontró solución.")



'''