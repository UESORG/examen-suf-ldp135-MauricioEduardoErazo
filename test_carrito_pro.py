import pytest
from carrito_pro import *

def test_json_ok():
    assert importar_y_validar_orden('{"items":[1],"total":10}')["total"]==10
def test_json_fail():
    assert importar_y_validar_orden('{"items":[1]}') is None
def test_pila():
    p=[]; gestionar_historial_carrito(p,"AGREGAR","A"); assert gestionar_historial_carrito(p,"DESHACER")=="A"
def test_matriz():
    assert escanear_estanteria_bodega([[1,1],[0,1]],0,0)==3
def test_rec():
    a={"cliente_frecuente":False,"izquierda":{"porcentaje_final":5},"derecha":{"porcentaje_final":10}}
    assert calcular_descuento_cascada(a)==5
def test_sort_search():
    l=ordenar_productos_quicksort([{"precio":3},{"precio":1},{"precio":2}])
    assert [x["precio"] for x in l]==[1,2,3]
    assert buscar_precio_binario(l,2)==1
