n = int(input("Ingrese el número de empleados: "))

sueldo_100_300 = 0
sueldoMas_300 = 0
totalGastos = 0
contador = 0

while contador < n:
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    if 100 <= sueldo <= 300:
        sueldo_100_300 += 1
    elif sueldo > 300:
        sueldoMas_300 += 1
    totalGastos += sueldo
    contador += 1

print(f"Cantidad de empleados que cobran entre $100 y $300: {sueldo_100_300}")
print(f"Cantidad de empleados que cobran más de $300: {sueldoMas_300}")
print(f"Total de gastos en sueldos: ${totalGastos:.2f}")
