n = int(input("Ingrese la cantidad de números enteros: "))

contarPares = 0
contarImpares = 0
contador = 0

while contador < n:
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    if numero % 2 == 0:
        contarPares += 1
    else:
        contarImpares += 1
    contador += 1

# Mostrar el resultado
print(f"Cantidad de números pares: {contarPares}")
print(f"Cantidad de números impares: {contarImpares}")
