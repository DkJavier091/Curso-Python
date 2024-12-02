"""
Escribir un programa que pida ingresar la coordenada de un punto en el plano,
es decir dos valores enteros x e y (distintos a cero).
Posteriormente, imprimir en pantalla en que cuadrante se ubica dicho punto.
(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""

x = int(input("Ingrese la coordenada x (distinta de cero): "))
y = int(input("Ingrese la coordenada y (distinta de cero): "))

if x > 0 and y > 0:
    cuadrante = "1º Cuadrante"
elif x < 0 and y > 0:
    cuadrante = "2º Cuadrante"
elif x < 0 and y < 0:
    cuadrante = "3º Cuadrante"
elif x > 0 and y < 0:
    cuadrante = "4º Cuadrante"
else:
    cuadrante = "No se encuentra en ningún cuadrante específico (debería ser distinto de cero)"

print(f"El punto está en el {cuadrante}")

