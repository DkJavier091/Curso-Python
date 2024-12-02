"""
Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10,
imprimir en pantalla la leyenda "Todos los números son menores a diez".
"""

num1 = float(input("Ingrese un número (1-3): "))
num2 = float(input("Ingrese un número (2-3): "))
num3 = float(input("Ingrese un número (3-3): "))


if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los números son menores a 10.")
