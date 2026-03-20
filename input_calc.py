def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))

    print (f"Base:", base)
    print(f"Altura: {altura}")
    area = base * altura
    print(f"Area: {area}")
    perimetro = (base + altura) * 2
    print(f"Perimetro: {perimetro}")

#rectangle()