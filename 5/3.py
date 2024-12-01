"""
Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.
"""

suma = 0
promedio = 0

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
numero4 = int(input("Introduce el cuarto número: "))

suma = numero1 + numero2 + numero3 + numero4
promedio = suma / 4

print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")