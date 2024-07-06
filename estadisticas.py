import globales
import math

def promedio_valor():
    todos_los_productos = globales.leer_archivo_json("productos.json")
    
    cantidad = 0
    suma = 0
    for producto in todos_los_productos:
        suma += int(producto["valor"])
        cantidad += 1

    promedio = suma / cantidad

    print("El promedio de venta es $", int(promedio))    

promedio_valor()


def media_geometrica():
    todos_los_productos = globales.leer_archivo_json("productos.json")
    
    cantidad = 0
    suma = 0
    for producto in todos_los_productos:
        suma += math.log( int(producto["valor"]))
        cantidad += 1

    promedio = suma / cantidad

    print("La media geometrica de venta es $", int(promedio))    

media_geometrica()


def valor_mas_alto():
    todos_los_productos = globales.leer_archivo_json("productos.json")

    productos_ordenados = sorted(todos_los_productos, key=lambda x: x('valor'), reverse=True )

    for producto in productos_ordenados[:1]:
        print("nombre:", producto['nombre'])
        print("valor", producto ['valor'])
        return
    
def valor_mas_bajo():
    todos_los_productos = globales.leer_archivo_json("productos.json")

    productos_ordenados = sorted(todos_los_productos, key=lambda x: x('iva'), reverse=False )

    for producto in productos_ordenados[:1]:
        print("nombre:", producto['nombre'])
        print("IVA", producto ['iva'])
        return

