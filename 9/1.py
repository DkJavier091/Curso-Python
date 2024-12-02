"""
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
continuar = True
notasSuperioresIguales7 = 0
notasInferiores7 = 0
contador = 0

while continuar:

    nota = float(input("Ingrese su nota (1/10): "))
    if nota >= 7:
        notasSuperioresIguales7 += 1
    else:
        notasInferiores7 += 1

    contador += 1

    if contador == 10:
        continuar = False

print(f"Se encuentran {notasSuperioresIguales7} notas superiores y iguales a 7.")
print(f"Se encuentran {notasInferiores7} notas inferiores a 7.")
