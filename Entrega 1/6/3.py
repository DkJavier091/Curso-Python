"""
Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""

numero = int(input("Ingrese un número positivo de 0 a mayor: "))
if numero >= 100:
    print("El número dispone de 3 o más dígitos.")
elif numero > 10:
    print("El número dispone de 2 dígitos.")
elif numero <= 9:
    print("El número dispone de 1 dígito.")

