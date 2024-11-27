# Ejercicio 3.3.1
# Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
# la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). 
# Ejemplo:
# [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
# Escribir una función que reciba como parámetro una lista con el formato mencionado 
# anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
# Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que 
# la función debe retornar una estructura que contenga cada domicilio una sola vez.


informacion_ventas = [
                    ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), 
                    ("Jorge Russo", 7, 699, "Mirasol 218"), 
                    ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), 
                    ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
                    ("Jorge Russo", 15, 958, "Mirasol 218")
                    ]


def direccion_facturas(lista_clientes: list[tuple]) -> set:
    """
    Obtiene una lista de tuplas y las añade a un set vacío para evitar repetidos.

    Args:
        lista_clientes (list[tuple]): Una lista de tuplas.

    Returns:
        domicilio_facturas (tuple): Un conjunto con las direcciones de los clientes.
    """
    domicilio_facturas = set()

    for ventas in lista_clientes:
        domicilio_facturas.add(ventas[3])

    return domicilio_facturas


def mostrar_direcciones(domicilios: set) -> str:
    """
    Muestra las direcciones en formato cadena.

    Args:
        domicilios (set): Un conjunto con las direcciones de los clientes.
    
    Returns:
        str: Una cadena con las direcciones de los clientes.
    """
    start = "DOMICILIOS A ENVIAR FACTURA\n---------------\n"
    cadena = "\n".join(map(str, domicilios))

    return start + cadena


def main():
    lista_clientes = direccion_facturas(informacion_ventas)
    print(mostrar_direcciones(lista_clientes))


if __name__ == "__main__":
    main()