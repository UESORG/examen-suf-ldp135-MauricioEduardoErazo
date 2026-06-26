import json


def importar_y_validar_orden(json_orden):
    """
    Objetivo: Decodificar un JSON, verificar si existen las llaves
    "items" y "total" (lanzar KeyError si no), y validar que "total"
    sea mayor a 0 (lanzar ValueError si no). Atrapar los errores y
    retornar None en caso de fallo, o el diccionario si es exitoso.
    """
    try:
        orden = json.loads(json_orden)

        if "items" not in orden or "total" not in orden:
            raise KeyError("La orden debe contener las llaves 'items' y 'total'.")

        total = orden["total"]

        if total <= 0:
            raise ValueError("El 'total' de la orden debe ser mayor a 0.")

        return orden

    except (json.JSONDecodeError, KeyError, ValueError, TypeError):
        return None


def gestionar_historial_carrito(historial_pila, accion, item=None):
    """
    Objetivo: Manejar una lista por referencia como una Pila (LIFO).
    Si la acción es "AGREGAR", insertar el ítem al final. Si es
    "DESHACER", extraer y retornar el último ítem (o retornar None
    si está vacía).
    """
    resultado = None

    if accion == "AGREGAR":
        historial_pila.append(item)
        resultado = item
    elif accion == "DESHACER":
        if len(historial_pila) == 0:
            resultado = None
        else:
            resultado = historial_pila.pop()

    return resultado


def escanear_estanteria_bodega(matriz_bodega, fila_centro, col_centro):
    """
    Objetivo: Analizar una matriz bidimensional (vecindad de 3x3)
    alrededor de una coordenada, respetando los límites para evitar
    desbordamientos, y retornar cuántos 1s existen en esa área.
    """
    contador_unos = 0
    filas_totales = len(matriz_bodega)

    for desplazamiento_fila in range(-1, 2):
        for desplazamiento_col in range(-1, 2):
            fila_actual = fila_centro + desplazamiento_fila
            col_actual = col_centro + desplazamiento_col

            if fila_actual < 0 or fila_actual >= filas_totales:
                continue

            columnas_totales = len(matriz_bodega[fila_actual])

            if col_actual < 0 or col_actual >= columnas_totales:
                continue

            if matriz_bodega[fila_actual][col_actual] == 1:
                contador_unos += 1

    return contador_unos


def calcular_descuento_cascada(nodo_descuento):
    """
    Objetivo: Recorrer un árbol binario de diccionarios. Si el nodo
    actual tiene "porcentaje_final", retornarlo (Caso Base). Si
    "cliente_frecuente" es True, bajar recursivamente por "derecha",
    de lo contrario, por "izquierda".
    """
    if nodo_descuento is None:
        return None

    if "porcentaje_final" in nodo_descuento:
        return nodo_descuento["porcentaje_final"]

    if nodo_descuento.get("cliente_frecuente") is True:
        return calcular_descuento_cascada(nodo_descuento.get("derecha"))
    else:
        return calcular_descuento_cascada(nodo_descuento.get("izquierda"))


def ordenar_productos_quicksort(lista_items):
    """
    Objetivo: Ordenar una lista de diccionarios según su llave
    "precio" de menor a mayor implementando QuickSort.
    """
    if len(lista_items) <= 1:
        return lista_items

    pivote = lista_items[0]
    resto = lista_items[1:]

    menores = [item for item in resto if item["precio"] <= pivote["precio"]]
    mayores = [item for item in resto if item["precio"] > pivote["precio"]]

    return ordenar_productos_quicksort(menores) + [pivote] + ordenar_productos_quicksort(mayores)


def buscar_precio_binario(lista_ordenada, precio_buscado):
    """
    Objetivo: Buscar la posición de un precio en la lista previamente
    ordenada de manera logarítmica. Retorna el índice, o -1 si no
    existe.
    """
    puntero_inicio = 0
    puntero_fin = len(lista_ordenada) - 1

    while puntero_inicio <= puntero_fin:
        puntero_medio = (puntero_inicio + puntero_fin) // 2
        precio_actual = lista_ordenada[puntero_medio]["precio"]

        if precio_actual == precio_buscado:
            return puntero_medio
        elif precio_actual < precio_buscado:
            puntero_inicio = puntero_medio + 1
        else:
            puntero_fin = puntero_medio - 1

    return -1
