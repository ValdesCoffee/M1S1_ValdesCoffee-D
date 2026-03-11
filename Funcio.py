#Declaremos las variables para indexar
import time 
import sys
for i in range(1, 11):
        time.sleep(0.3) # El efecto de "carga"
        sys.stdout.write("\r****************""")
        sys.stdout.flush()
        #Este mensaje busca ser amigable con el usuario,Esta pegado con "\n" Para no hacer tantos prints
        nombredeproduct= input("\nHola ¡Bienvenido al Inventario!\nIngrese su producto: ")     
         #Pide el precio como un número real
        preciodeproduct= float(input("Coloque el precio de su producto: "))      
        #Pide la cantidad como un numero entero (ya que no existe dame 2.5 de manzanas)
        cantidadproduct= int(input("Coloca la cantidad de productos: "))   