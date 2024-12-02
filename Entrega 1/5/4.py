"""
Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.
"""

horasTrabajadas = 0.0
precioHora = 0.0
sueldoDiario = 0.0
sueldoSemanal = 0.0
sueldoMensual = 0.0

horasTrabajadas = float(input("Ingresa el número de horas trabajadas: "))
precioHora = float(input("Ingresa el precio por hora: "))

sueldoDiario = horasTrabajadas * precioHora
sueldoSemanal = sueldoDiario * 7
sueldoMensual = sueldoSemanal + 4


print(f"El sueldo mensual es: {sueldoMensual}")