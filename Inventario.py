#Declaremos las variables para indexar
import time 
import sys
# Bucle infinito: el programa seguirá ejecutándose hasta que el usuario decida salir
while True:
     # El efecto de "carga"
    time.sleep(0.3) 
    sys.stdout.write("\r****************""")
    sys.stdout.flush()
     # Se le pide al usuario el nombre del producto.
     # "\n" agrega un salto de línea para que el mensaje se vea más ordenado en consola
    nameofproduct = input("\nHola ¡Bienvenido al Inventario!\nIngrese su producto: ")

     # Se pide el precio del producto.
     # input siempre devuelve texto, por eso se convierte a float (número decimal)
    priceofproduct = float(input("Coloque el precio de su producto: "))

     # Se pide la cantidad de productos.
     # Se convierte a int porque la cantidad normalmente es un número entero
    productquantity = int(input("Coloca la cantidad de productos: "))

     # Se calcula el valor total multiplicando precio por cantidad
    Total = priceofproduct * productquantity

     # Se muestra el resultado al usuario
     # f permite insertar variables dentro del texto
    print(f"Tu", nameofproduct, "vale", Total)

     # Se pregunta al usuario si desea seguir ingresando productos
     # .lower() convierte la respuesta a minúsculas para evitar problemas
     # por ejemplo "Si", "SI", "si" se interpretan igual
    chosecontinue = input("¿Deseas seguir? (Si/No): ").lower()

     # Si el usuario escribe algo diferente a "si"
     # el programa rompe el bucle infinito
     # y el programa termina
    if chosecontinue != "si":

          break
