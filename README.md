# .✦ ݁˖ Calculadora de Inventario  
𐔌՞ ܸ.ˬ.ܸ՞𐦯

Este es un pequeño programa que busca que los emprendimientos tengan una mejor manera de contablizar sus productos.
Algunos requerimentos basicos para ejecutarse:
- Tener python
- Tener un lector de python

¿Que te solicita el programa?
El programa solicita:
- Nombre del producto  
- Precio del producto  
- Cantidad  

Luego calcula el **valor total** con la siguiente operacion
```python3
 Total = priceofproduct * productquantity 
```
 y pregunta si el usuario desea continuar ingresando productos.

---

## ݁🐇Usables

- Python 3  
- Librerías usadas: `time`, `sys` (incluidas en Python)

---
## Funcionalidades del programa

Este programa funciona como una pequeña herramienta de inventario ejecutada desde la consola. Su objetivo principal es permitir al usuario ingresar información sobre un producto y calcular automáticamente su valor total dentro del inventario.

### 🐇Funciones principales

**Ingreso de datos:**  
El programa solicita al usuario el nombre del producto, el precio y la cantidad disponible. Estos datos se ingresan directamente desde la consola utilizando la función `input()`.

**Conversión de tipos de datos:**  
Los valores ingresados se convierten a los tipos adecuados para poder trabajar con ellos correctamente. El precio se convierte a `float` y la cantidad a `int`.

**Cálculo del valor total:**  
El sistema calcula el valor total del producto multiplicando el precio por la cantidad ingresada por el usuario.

**Ejecución continua:**  
El programa utiliza un bucle `while` para permitir que el usuario pueda registrar múltiples productos sin necesidad de reiniciar el programa.

**Control de salida:**  
Al finalizar cada operación, el sistema pregunta al usuario si desea continuar. Si la respuesta es diferente de "si", el programa termina su ejecución.

## ▶️ Ejecutar el programa

```bash
python inventario.py
```
