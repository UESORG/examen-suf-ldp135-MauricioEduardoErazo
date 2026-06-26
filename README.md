[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/66UDLJ0P)
# Examen_Complementario_LDP2026
# Carnet:EJ24004 
# Nombre: Mauricio Eduardo Erazo Juarez
# Grupo: GT3 Horario: Sábado de 9:15 a 10:55 am
# Aplicacion: E-Commerce Pro

## Archivos
##===========================================
### carrito_pro.py

1. importar_y_validar_orden(json_orden)

Recibe una cadena JSON y la decodifica con json.loads. Dentro de un
bloque try/except, verifica que existan las llaves "items" y
"total" (lanzando KeyError si falta alguna) y que "total" sea
mayor a 0 (lanzando ValueError en caso contrario). Si el JSON está
corrupto o se lanza cualquiera de esas excepciones, la función las
atrapa y retorna None. Si todo es válido, retorna el diccionario de
la orden ya decodificado.

2. gestionar_historial_carrito(historial_pila, accion, item=None)

Trata la lista historial_pila como una Pila (LIFO), mutándola
por referencia (no crea una copia, modifica la lista original que se
le pasa). Con if/elif:


"AGREGAR" → inserta item al final con append.
"DESHACER" → extrae y retorna el último ítem con pop, o
retorna None si la pila está vacía.


3. escanear_estanteria_bodega(matriz_bodega, fila_centro, col_centro)

Recorre con dos ciclos for anidados la vecindad de 3x3 alrededor de
la coordenada (fila_centro, col_centro) dentro de la matriz
matriz_bodega. Antes de leer cada celda valida los límites de filas
y columnas para evitar desbordamientos (IndexError). Usa una
variable acumuladora (contador_unos) que incrementa cada vez que
encuentra un 1, y la retorna al final.

4. calcular_descuento_cascada(nodo_descuento)

Recorre recursivamente un árbol binario representado con
diccionarios anidados ("izquierda" / "derecha"):


Caso base: si el nodo actual tiene la llave
"porcentaje_final", la retorna.
Caso recursivo: si "cliente_frecuente" es True, baja por
"derecha"; en caso contrario, baja por "izquierda", llamándose
a sí misma hasta llegar al caso base.


5. ordenar_productos_quicksort(lista_items)

Implementa QuickSort sobre una lista de diccionarios, usando la
llave "precio" de cada uno como criterio de orden (de menor a
mayor). Toma el primer elemento como pivote, construye por
comprensión las sublistas de menores y mayores respecto al
pivote, y se llama recursivamente sobre cada sublista hasta que el
caso base (lista_items de tamaño 0 o 1) detiene la recursión.

6. buscar_precio_binario(lista_ordenada, precio_buscado)

Implementa búsqueda binaria sobre una lista de diccionarios ya
ordenada por "precio". Usa dos punteros numéricos
(puntero_inicio, puntero_fin) que delimitan el rango de búsqueda
y un while que se repite mientras el rango sea válido. En cada
iteración calcula el punto medio (puntero_medio) y, con
if/elif/else, decide si el precio buscado está a la izquierda, a la
derecha o si ya fue encontrado. Retorna el índice del precio
encontrado, o -1 si no existe en la lista.


test_carrito_pro.py

Usa pytest para validar el comportamiento de las 6 funciones
anteriores, cubriendo los siguientes escenarios:


JSON corruptos: cadenas mal formadas, sin la llave "items",
sin la llave "total", o con "total" igual a 0 o negativo —
todos estos casos deben retornar None.
Mutación de pilas: se verifica que gestionar_historial_carrito
modifique la lista original (por referencia) tanto al agregar como
al deshacer, y que "DESHACER" sobre una pila vacía retorne None
sin lanzar errores.
Límites de matrices: se prueba el escaneo desde el centro de la
matriz y desde sus esquinas (donde algunos vecinos caerían fuera de
rango), confirmando que la función nunca intenta acceder a índices
inválidos y cuenta los 1 correctamente.
Casos base recursivos: se valida que
calcular_descuento_cascada retorne de inmediato cuando el nodo ya
tiene "porcentaje_final", y que descienda correctamente por
"derecha" o "izquierda" según "cliente_frecuente", incluso en
árboles de varios niveles.
Eficiencia de ordenamiento y búsqueda: se prueba
ordenar_productos_quicksort con listas vacías, de un elemento, con
precios repetidos y con varios productos desordenados; luego se
combina con buscar_precio_binario para confirmar que, una vez
ordenada la lista, la búsqueda binaria localiza correctamente el
producto buscado (o retorna -1 si el precio no existe).

## Ejecutar pruebas

```bash
pytest test_carrito_pro.py -v
