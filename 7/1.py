"""
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
"""

num1 = float(input("Ingrese el primer número de 3: "))
num2 = float(input("Ingrese el segundo número de 3: "))
num3 = float(input("Ingrese el tercer número de 3: "))

if num1 == num2 == num3:
    print("Los tres son iguales!")

if num1 > num2:
    if num1 > num3:
        print(f"El mayor de ellos es {num1}")
    else:
        print(f"El mayor de ellos es {num3}")
elif num2 > num3:
        print(f"El mayor de ellos es {num2}")
else:
        print(f"El mayor de ellos es {num3}")
