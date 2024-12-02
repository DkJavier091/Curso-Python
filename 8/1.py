"""
Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.
"""

dia = int(input("Ingrese un día del mes (1-31): "))
mes = int(input("Ingrese un números de mes (1 (Enero)-12 (Diciembre): "))

if dia == 0 or mes == 0 or dia > 31 or mes > 12:
    print("Compruebe los datos ingresados, uno o varios no coinciden con los requisitos marcados...")
elif dia == 25 and mes == 12:
    print("Se ha introducido la fecha de navidad! \nFeliz Navidad!")