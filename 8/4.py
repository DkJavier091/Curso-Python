"""
Se ingresan tres valores por teclado,
si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.
"""

num1 = float(input("Ingrese un número (1-3): "))
num2 = float(input("Ingrese un número (2-3): "))
num3 = float(input("Ingrese un número (3-3): "))


if num1 == num2 == num3:
    suma = num1 + num2
    resultado = suma * num3
    print("El resultado es: ", resultado)

