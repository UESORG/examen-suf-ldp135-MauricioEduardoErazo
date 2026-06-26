import json
import pytest

from carrito_pro import (
    importar_y_validar_orden,
    gestionar_historial_carrito,
    escanear_estanteria_bodega,
    calcular_descuento_cascada,
    ordenar_productos_quicksort,
    buscar_precio_binario,
)


# ---------------------------------------------------------------------
# importar_y_validar_orden
# ---------------------------------------------------------------------

def test_importar_orden_exitosa():
    json_orden = json.dumps({"items": ["mouse", "teclado"], "total": 49.99})
    resultado = importar_y_validar_orden(json_orden)
    assert resultado is not None
    assert resultado["total"] == 49.99
    assert resultado["items"] == ["mouse", "teclado"]


def test_importar_orden_json_corrupto():
    json_corrupto = "{items: [mouse, teclado], total: 49.99"  # JSON inválido
    resultado = importar_y_validar_orden(json_corrupto)
    assert resultado is None


def test_importar_orden_sin_llave_items():
    json_orden = json.dumps({"total": 49.99})
    resultado = importar_y_validar_orden(json_orden)
    assert resultado is None


def test_importar_orden_sin_llave_total():
    json_orden = json.dumps({"items": ["mouse"]})
    resultado = importar_y_validar_orden(json_orden)
    assert resultado is None


def test_importar_orden_total_negativo():
    json_orden = json.dumps({"items": ["mouse"], "total": -10})
    resultado = importar_y_validar_orden(json_orden)
    assert resultado is None


def test_importar_orden_total_cero():
    json_orden = json.dumps({"items": ["mouse"], "total": 0})
    resultado = importar_y_validar_orden(json_orden)
    assert resultado is None


# ---------------------------------------------------------------------
# gestionar_historial_carrito (mutación de pilas)
# ---------------------------------------------------------------------

def test_agregar_item_muta_la_lista_por_referencia():
    historial = []
    gestionar_historial_carrito(historial, "AGREGAR", "laptop")
    assert historial == ["laptop"]


def test_agregar_varios_items_orden_lifo():
    historial = []
    gestionar_historial_carrito(historial, "AGREGAR", "laptop")
    gestionar_historial_carrito(historial, "AGREGAR", "mouse")
    assert historial == ["laptop", "mouse"]


def test_deshacer_extrae_el_ultimo_item():
    historial = ["laptop", "mouse"]
    item_extraido = gestionar_historial_carrito(historial, "DESHACER")
    assert item_extraido == "mouse"
    assert historial == ["laptop"]


def test_deshacer_con_pila_vacia_retorna_none():
    historial = []
    resultado = gestionar_historial_carrito(historial, "DESHACER")
    assert resultado is None
    assert historial == []


# ---------------------------------------------------------------------
# escanear_estanteria_bodega (límites de matrices)
# ---------------------------------------------------------------------

def test_escanear_centro_de_matriz():
    matriz = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    resultado = escanear_estanteria_bodega(matriz, 1, 1)
    assert resultado == 5  # cuatro esquinas con 1 + el centro


def test_escanear_esquina_superior_izquierda_no_desborda():
    matriz = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    # La coordenada (0,0) obliga a revisar índices negativos
    resultado = escanear_estanteria_bodega(matriz, 0, 0)
    assert resultado == 2  # (0,0) y (1,1)


def test_escanear_esquina_inferior_derecha_no_desborda():
    matriz = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    resultado = escanear_estanteria_bodega(matriz, 2, 2)
    assert resultado == 2  # (1,1) y (2,2)


def test_escanear_sin_unos_retorna_cero():
    matriz = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    resultado = escanear_estanteria_bodega(matriz, 1, 1)
    assert resultado == 0


# ---------------------------------------------------------------------
# calcular_descuento_cascada (casos base recursivos)
# ---------------------------------------------------------------------

def test_descuento_caso_base_directo():
    nodo = {"porcentaje_final": 10}
    assert calcular_descuento_cascada(nodo) == 10


def test_descuento_cliente_frecuente_baja_por_derecha():
    arbol = {
        "cliente_frecuente": True,
        "derecha": {"porcentaje_final": 25},
        "izquierda": {"porcentaje_final": 5},
    }
    assert calcular_descuento_cascada(arbol) == 25


def test_descuento_cliente_no_frecuente_baja_por_izquierda():
    arbol = {
        "cliente_frecuente": False,
        "derecha": {"porcentaje_final": 25},
        "izquierda": {"porcentaje_final": 5},
    }
    assert calcular_descuento_cascada(arbol) == 5


def test_descuento_recursivo_en_varios_niveles():
    arbol = {
        "cliente_frecuente": True,
        "derecha": {
            "cliente_frecuente": False,
            "izquierda": {"porcentaje_final": 40},
            "derecha": {"porcentaje_final": 60},
        },
        "izquierda": {"porcentaje_final": 5},
    }
    assert calcular_descuento_cascada(arbol) == 40


# ---------------------------------------------------------------------
# ordenar_productos_quicksort (eficiencia de ordenamiento)
# ---------------------------------------------------------------------

def test_quicksort_ordena_de_menor_a_mayor():
    productos = [
        {"nombre": "monitor", "precio": 150},
        {"nombre": "mouse", "precio": 20},
        {"nombre": "laptop", "precio": 900},
        {"nombre": "teclado", "precio": 45},
    ]
    resultado = ordenar_productos_quicksort(productos)
    precios = [p["precio"] for p in resultado]
    assert precios == [20, 45, 150, 900]


def test_quicksort_lista_vacia():
    assert ordenar_productos_quicksort([]) == []


def test_quicksort_lista_de_un_elemento():
    productos = [{"nombre": "mouse", "precio": 20}]
    assert ordenar_productos_quicksort(productos) == productos


def test_quicksort_con_precios_repetidos():
    productos = [
        {"nombre": "a", "precio": 10},
        {"nombre": "b", "precio": 10},
        {"nombre": "c", "precio": 5},
    ]
    resultado = ordenar_productos_quicksort(productos)
    precios = [p["precio"] for p in resultado]
    assert precios == [5, 10, 10]


# ---------------------------------------------------------------------
# buscar_precio_binario (eficiencia de búsqueda)
# ---------------------------------------------------------------------

def test_busqueda_binaria_encuentra_precio_existente():
    lista_ordenada = [
        {"nombre": "mouse", "precio": 20},
        {"nombre": "teclado", "precio": 45},
        {"nombre": "monitor", "precio": 150},
        {"nombre": "laptop", "precio": 900},
    ]
    assert buscar_precio_binario(lista_ordenada, 150) == 2


def test_busqueda_binaria_precio_inexistente_retorna_menos_uno():
    lista_ordenada = [
        {"nombre": "mouse", "precio": 20},
        {"nombre": "teclado", "precio": 45},
        {"nombre": "monitor", "precio": 150},
    ]
    assert buscar_precio_binario(lista_ordenada, 999) == -1


def test_busqueda_binaria_lista_vacia():
    assert buscar_precio_binario([], 100) == -1


def test_busqueda_binaria_primer_y_ultimo_elemento():
    lista_ordenada = [
        {"nombre": "a", "precio": 1},
        {"nombre": "b", "precio": 2},
        {"nombre": "c", "precio": 3},
    ]
    assert buscar_precio_binario(lista_ordenada, 1) == 0
    assert buscar_precio_binario(lista_ordenada, 3) == 2


def test_integracion_quicksort_y_busqueda_binaria():
    productos = [
        {"nombre": "monitor", "precio": 150},
        {"nombre": "mouse", "precio": 20},
        {"nombre": "laptop", "precio": 900},
        {"nombre": "teclado", "precio": 45},
    ]
    ordenados = ordenar_productos_quicksort(productos)
    indice = buscar_precio_binario(ordenados, 45)
    assert ordenados[indice]["nombre"] == "teclado"
