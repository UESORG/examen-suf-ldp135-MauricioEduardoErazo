[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/66UDLJ0P)
# Examen_Complementario_LDP2026
# Carnet:EJ24004 
# Nombre: Mauricio Eduardo Erazo Juarez
# Grupo: GT3 Horario: Sábado de 9:15 a 10:55 am
# Aplicacion: E-Commerce Pro

## Archivos
##===========================================
### carrito_pro.py

Contiene las funciones principales del backend:

1. importar_y_validar_orden()
   - Valida órdenes JSON.

2. gestionar_historial_carrito()
   - Implementa una pila LIFO para historial.

3. escanear_estanteria_bodega()
   - Analiza una matriz y cuenta productos cercanos.

4. calcular_descuento_cascada()
   - Recorre un árbol binario mediante recursividad.

5. ordenar_productos_quicksort()
   - Ordena productos usando QuickSort.

6. buscar_precio_binario()
   - Busca precios mediante búsqueda binaria.

### test_carrito_pro.py

Contiene pruebas unitarias realizadas con pytest para:

- JSON válidos e inválidos.
- Operaciones de pila.
- Límites de matrices.
- Casos recursivos.
- Ordenamiento QuickSort.
- Búsqueda binaria.

## Ejecutar pruebas

```bash
pytest test_carrito_pro.py -v
