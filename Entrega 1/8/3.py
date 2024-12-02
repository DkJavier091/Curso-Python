"""
Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10,
imprimir en pantalla la leyenda "Alguno de los números es menor a diez".
"""

num1 = float(input("Ingrese un número (1-3): "))
num2 = float(input("Ingrese un número (2-3): "))
num3 = float(input("Ingrese un número (3-3): "))


if num1 < 10 or num2 < 10 or num3 < 10:
    print("Alguno de los números es menor a 10.")
