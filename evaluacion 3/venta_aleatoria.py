import os
import globales 
import random 

productos = [
    "Café Americano",
    "Té Chai",
    "Croissant",
    "Jugo Naranja",
    "Panini de Pavo y Queso",
    "Pastel de Zanahoria",
    "Espresso Doble",
    "Ba;do de Frutas",
    "Muffin",
    "Ensalada",
    "Chocolate Caliente",
    "Tarta de Frambuesa",
    "Sándwich de Huevo",
    "Galletas de Avena",
    "Frappé de Caramelo"
]

def venta_aleatoria():
    empleados = []
    for producto in productos:
        nombre= random.choice(productos)        
        valor= random.choice(2000, 10000)
        iva =  int(valor*0.19)

        valor_random = 


    