sumaLista1 = 0
sumaLista2 = 0

print("Ingrese 15 valores para la lista 1:")
contador = 0
while contador < 15:
    valor = float(input(f"Ingrese el valor {contador + 1}: "))
    sumaLista1 += valor
    contador += 1

print("Ingrese 15 valores para la lista 2:")
contador = 0
while contador < 15:
    valor = float(input(f"Ingrese el valor {contador + 1}: "))
    sumaLista2 += valor
    contador += 1

if sumaLista1 > sumaLista2:
    print("Lista 1 mayor")
elif sumaLista2 > sumaLista1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")
