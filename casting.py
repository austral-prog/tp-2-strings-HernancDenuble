def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento: "))
    cantidad = int(input("Ingrese el cantidad: "))

    print (f"Precio: {precio}")
    print (f"Descuento: {descuento}")
    precio_con_descuento = precio - descuento
    print (f"Precio con descuento: {precio_con_descuento}")
    precio_total = precio_con_descuento * cantidad
    print (f"Total: {precio_total}")

#casting()