"""
Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e
informe su rango de variación (debe mostrar el mayor y el menor de ellos)
"""

valor1 = float(input("Ingrese el primer valor numérico: "))
valor2 = float(input("Ingrese el segundo valor numérico: "))
valor3 = float(input("Ingrese el tercer valor numérico: "))

if valor1 > valor2 and valor1 > valor3:
    mayor = valor1
elif valor2 > valor1 and valor2 > valor3:
    mayor = valor2
else:
    mayor = valor3

if valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor1 and valor2 < valor3:
    menor = valor2
else:
    menor = valor3

print(f"El mayor valor es: {mayor}")
print(f"El menor valor es: {menor}")
