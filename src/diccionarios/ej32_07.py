# Ejercicio 3.2.7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
# Lista de la compra 	
# Artículo 1 	Precio
# Artículo 2 	Precio
# Artículo 3 	Precio
# … 	…
# Total 	Coste


def pedir_productos():
    """
    Pide productos al usuario hasta que el usuario desee terminar introduciendo "S", retornando un diccionario con Articulo-Producto.
    """

    # Inicializa diccionario clave-valor vacío para los productos.
    productos = {}
    
    # Variable de control para saber si debe pedir productos o no.
    pedir_productos = True
    while pedir_productos:
        pedir_productos = input("¿Desea añadir productos al carrito? (n para salir) >> ").upper().strip()
        if pedir_productos == "N":
            pedir_productos = False
            return productos
        else:
            # if True, pide productos, si no pasa el try-catch vuelve a pedir S/N para salir sin actualizar el dict.
            pedir_productos = True
            try:
                nombre_producto = str(input("Introduce el nombre del producto >> ")).capitalize().strip()
                precio_producto = int(input("Introduce el precio del producto >> "))
                productos.update({nombre_producto: precio_producto})
            except ValueError:
                pedir_productos = True
                print("*ERROR* El precio debe ser un número.")

    return productos


def mostrar_productos(productos: dict):
    """
    
    """
    productos_totales = contar_productos(productos)
    precio_total = sumar_precio_productos(productos)
    productos_string = "Lista de la compra\n"

    # Artículo 1 	Precio
    # Artículo 2 	Precio
    # Artículo 3 	Precio
    # … 	…
    # Total 	Coste

    for producto, precio in productos.items():
        productos_string += f"{producto}    {precio} €\n"
    
    productos_string += f"{productos_totales}   {precio_total} €"

    return productos_string


def contar_productos(productos: dict):
    """
    
    """
    cantidad_productos = 0

    for _ in productos:
        cantidad_productos += 1

    return cantidad_productos


def sumar_precio_productos(productos: dict):
    """
    
    """
    precio_total = 0

    for producto in productos.values():
        precio_total+= producto
    
    return precio_total


def main():
    productos = pedir_productos()

    print(mostrar_productos(productos))


if __name__ == "__main__":
    main()