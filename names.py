def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    name1 = input("Ingrese su nombre: ")
    name2 = input("Ingrese su apellido: ")

    nombre_completo = name1 + " " + name2
    print (nombre_completo.lower())
    print(nombre_completo.title())
    print(nombre_completo.upper())
    print(f"\t{nombre_completo.lower()}")

#names()
