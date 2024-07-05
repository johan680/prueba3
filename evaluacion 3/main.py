import os
import json
import globales 
import venta_aleatoria


def menu_general():
    print("1_asignar montos aleatorios")
    print("2_ ver estadisticas")
    print("3_ salir del programa ")
    
    try:
        opcion = globales.seleccionar_opcion(3)
    except:
        pass

    def menu_estadisticas():
        print("1_ Producto con valor mas alto")
        print("2_ Producto con el iva mas bajo")
        print("3_ Promedio del valor de los productos")
        print("4_ Media geometrica de valor de los productos")
        
        try:
            opcion = globales.seleccionar_opcion(4)
        except:
            pass

        if opcion == 1:
            print(" producto con valor mas alto")
        elif opcion == 2:
            print(" Producto con el iva mas bajo")
        elif opcion == 3:
            print(" Promedio del valor de los productos")        
        elif opcion == 4:
            print("Media geometrica de valor de los productos")

                


    
    
