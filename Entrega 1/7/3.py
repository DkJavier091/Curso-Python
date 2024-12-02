"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
Mostrar un mensaje de error si el número de cifras es mayor.
"""
num = int(input("Ingrese un número entero positivo. (máximo número posible 999): "))

if num > 999:
    print("!Hey no se permiten números mayores de 3 cifras!")
elif num == 0:
    print("El número es neutro...")
elif num < 0:
    print("!Hey no se permiten números negativos, han de ser enteros y positivos!")
elif num >= 100:
    print("El número dispone de 3 cifra.")
elif num >= 10:
    print("El número dispone de 2 cifras.")
else:
    print("El número dispone de 1 cifra.")

