def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.

Strip: Grace Hopper
Lstrip: Grace Hopper
Rstrip:    Grace Hopper
Upper: PYTHON ES UN GRAN LENGUAJE DE PROGRAMACION
Lower: python es un gran lenguaje de programacion
Title: Python Es Un Gran Lenguaje De Programacion
Find: 13
Replace: Python es un gran lenguaje de desarrollo
Count: 4
Contiene Python: True
Contiene Java: False
Slice: Python
Paso: Pto
Reverso: nohtyP
Formato: Grace Hopper sabe Python
Linea 1
Linea 2
Linea 3
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    print(f"Strip: {nombre.strip()}")
    print(f"Lstrip: {nombre.lstrip()}")
    print(f"Rstrip: {nombre.rstrip()}")
    print(f"Upper: {frase.upper()}")
    print(f"Lower: {frase.lower()}")
    print(f"Title: {frase.title()}")
    print(f"Find: {frase.find("gran")}")
    print(f"Replace: {frase.replace("programacion", "desarrollo")}")
    print(f"Count: {frase.count('a')}")
    print(f"Contiene Python: {("Python" in frase)}")
    print(f"Contiene Java: {("Java" in frase)}")
    print(f"Slice: {"Python"}")
    print(f"Paso: {frase[:6:2]}")
    print(f"Reverso: {frase[5::-1]}")
    print(f"Formato: {nombre.strip()} sabe Python")
    linea_1 = multilinea[0:7]
    linea_2 = multilinea[12:19]
    linea_3 = multilinea[24:31]
    print(linea_1)
    print(linea_2)
    print(linea_3)

#string_methods()