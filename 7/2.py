"""
Se ingresa por teclado un valor entero,
mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
"""

num = int(input("Ingrese un número entero: "))

if num == 0:
    print("Es neutro")
elif num > 0:
    print("Es positivo")
elif num < 0:
    print("Es negativo")