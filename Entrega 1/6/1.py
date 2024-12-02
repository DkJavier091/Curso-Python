"""
Realizar un programa que solicite la carga por teclado de dos números,
si el primero es mayor al segundo informar su suma y diferencia,
en caso contrario informar el producto y la división del primero respecto al segundo.
"""

numero1 = float(input("Introduzca el primer número: "))
numero2 = float(input("Introduzca el segundo número: "))

if numero1 > numero2:
    suma = numero1 + numero2
    diferencia = numero1 - numero2
    print(f"La suma es: {suma}, mientras que su diferencia es {diferencia}")
else:
    print(f"{numero2} es mayor a {numero1}")
    producto = numero1 * numero2
    division = numero1 / numero2
    print(f"El producto es: {producto}, mientras que su division es {division}")

