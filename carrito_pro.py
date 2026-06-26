import json

def importar_y_validar_orden(json_orden):
    try:
        orden = json.loads(json_orden)
        if "items" not in orden or "total" not in orden:
            raise KeyError
        if orden["total"] <= 0:
            raise ValueError
        return orden
    except (json.JSONDecodeError, KeyError, ValueError):
        return None

def gestionar_historial_carrito(historial_pila, accion, item=None):
    if accion=="AGREGAR":
        historial_pila.append(item)
        return historial_pila
    elif accion=="DESHACER":
        if historial_pila:
            return historial_pila.pop()
        return None
    return None

def escanear_estanteria_bodega(matriz_bodega,fila_centro,col_centro):
    c=0
    for i in range(max(0,fila_centro-1),min(len(matriz_bodega),fila_centro+2)):
        for j in range(max(0,col_centro-1),min(len(matriz_bodega[0]),col_centro+2)):
            if matriz_bodega[i][j]==1:
                c+=1
    return c

def calcular_descuento_cascada(nodo_descuento):
    if "porcentaje_final" in nodo_descuento:
        return nodo_descuento["porcentaje_final"]
    if nodo_descuento["cliente_frecuente"]:
        return calcular_descuento_cascada(nodo_descuento["derecha"])
    return calcular_descuento_cascada(nodo_descuento["izquierda"])

def ordenar_productos_quicksort(lista_items):
    if len(lista_items)<=1:
        return lista_items
    pivote=lista_items[0]
    menores=[x for x in lista_items[1:] if x["precio"]<=pivote["precio"]]
    mayores=[x for x in lista_items[1:] if x["precio"]>pivote["precio"]]
    return ordenar_productos_quicksort(menores)+[pivote]+ordenar_productos_quicksort(mayores)

def buscar_precio_binario(lista_ordenada,precio_buscado):
    izq=0; der=len(lista_ordenada)-1
    while izq<=der:
        m=(izq+der)//2
        if lista_ordenada[m]["precio"]==precio_buscado:
            return m
        elif lista_ordenada[m]["precio"]<precio_buscado:
            izq=m+1
        else:
            der=m-1
    return -1
