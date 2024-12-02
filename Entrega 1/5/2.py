"""
Escribir un programa en el cual se ingresen cuatro números,
calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto.
"""

suma = 0
producto = 0

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
numero4 = int(input("Introduce el cuarto número: "))

suma = numero1 + numero2
producto = numero3 * numero4

print(f"La suma de los dos primeros números da como resultado: {suma}")
print(f"El producto del tercer y cuarto número da como resultado: {producto}")

