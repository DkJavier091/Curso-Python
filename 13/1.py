oracion = input("Ingrese una oración: ")

contadorEspacios = 0
longitudOracion = len(oracion)
indice = 0

while indice < longitudOracion:
    if oracion[indice] == " ":
        contadorEspacios += 1
    indice += 1

print(f"La cantidad de espacios en blanco es: {contadorEspacios}")
