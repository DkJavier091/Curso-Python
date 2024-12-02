"""
De un operario se conoce su sueldo y los años de antigüedad.
Se pide confeccionar un programa que lea los datos de entrada e informe:

a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
otorgarle un aumento del 20 %, mostrar el sueldo a pagar.

b)Si el sueldo es inferior a 500, pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.

c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
"""

sueldo = float(input("Ingrese el sueldo del operario: "))
antiguedad = int(input("Ingrese los años de antigüedad del operario: "))

if sueldo < 500 and antiguedad >= 10:
    sueldo_final = sueldo * 1.20
elif sueldo < 500 and antiguedad < 10:
    sueldo_final = sueldo * 1.05
else:
    sueldo_final = sueldo

print(f"El sueldo a pagar es: {sueldo_final:.2f} euros") #.2f solo mostrará 2 decimales :D

