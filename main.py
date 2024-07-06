import os
import globales
import productos
import estadisticas

def menu_estadisticas():
    while True:
        os.system("cls")
        print("--- MENU ---")
        print("1. Producto con valor mas alto")
        print("2. producto con valor del iva mas bajo")
        print("3. promedio del valor de los productos")
        print("4_ media geometrica del valor de los productos")
        print("5_ salir del programa")

        opcion= globales.seleccionar_opcion(5)

        if opcion == 1:
            print("1. Producto con valor mas alto ")
            estadisticas.valor_mas_alto
        elif opcion == 2:
            print("2_ producto con valor del iva mas bajo")
            estadisticas.valor_mas_bajo
        elif opcion == 3:
            print("3_ promedio del valor de los productos")
            estadisticas.promedio_valor
        elif opcion == 4:
            print("4_ media geometrica del valor de los productos")
            estadisticas.media_geometrica  
        elif opcion == 5:
            print("5_ salir")     
            return

        input()


def menu_general():
    while True:
        os.system("cls")
        print("--- MENU ---")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa")

        opcion= globales.seleccionar_opcion(3)

        if opcion == 1:
            productos.generar_aleatorios()
        elif opcion == 2:
           menu_estadisticas()
        elif opcion == 3:
            print("3_ salir del programa")
            return

        input()



menu_general()
