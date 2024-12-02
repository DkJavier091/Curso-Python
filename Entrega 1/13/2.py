oracion = input("Ingrese una oración: ")

oracionMinusculas = oracion.lower()

contadorVocales = 0

indice = 0
longitudOracion = len(oracionMinusculas)
while indice < longitudOracion:
    if oracionMinusculas[indice] in "aeiou":
        contadorVocales += 1
    indice += 1

print(f"La cantidad de vocales es: {contadorVocales}")
