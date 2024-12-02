clave = input("Ingrese una clave: ")

longitudClave = len(clave)

if 10 <= longitudClave <= 20:
    print("Clave válida.")
else:
    print("Error: La clave debe tener entre 10 y 20 caracteres.")
