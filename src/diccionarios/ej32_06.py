# Ejercicio 3.2.6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


def validar_edad(edad: str) -> bool:
    """
    
    """
    try:
        edad = int(edad)
        if edad <= 0:
            raise Exception("*ERROR* La edad introducida no es válida.")
        return True

    except Exception as e:
        print(e)
        return False
    except ValueError:
        print("*ERROR* Debes introducir un número.")
        return False


def validar_telefono(tlf: str) -> bool:
    """
    Valida que el teléfono introducido sea válido.

    Args:
        tlf (str): El teléfono a validar.

    Returns:
        bool: True si el teléfono es válido, False en caso de no serlo.
    """
    try:
        if len(tlf) != 9:
            raise Exception("*ERROR* El teléfono no es válido.")
        int(tlf)
        return True

    except ValueError:
        print("*ERROR* No has introducido un número")
        return False

    except Exception as e:
        print(e)
        return False


def crear_diccionario() -> dict:
    """
    
    """

    informacion_cliente = {}

    nombre = input("Introduce tu nombre: ")
    informacion_cliente.update({'nombre': nombre})
    print(informacion_cliente)
    edad = input("Introduce tu edad: ")

    if validar_edad(edad):
        informacion_cliente.update({'edad': int(edad)})
    else:
        informacion_cliente.update({'edad': 99})
    print(informacion_cliente)

    direccion = input("Introduce tu dirección: ")
    informacion_cliente.update({'direccion': direccion})
    print(informacion_cliente)
    telefono = input("Introduce tu número de teléfono: ")

    if validar_telefono(telefono):
        informacion_cliente.update({'telefono': int(telefono)})
    else:
        informacion_cliente.update({'telefono': 999999999})

    print(informacion_cliente)

    return informacion_cliente


def mostrar_datos_usuario(informacion_cliente: dict) -> str:
    """
    
    """
    datos_usuario = "--- DATOS DEL USUARIO ---\n"

    datos_usuario += f"Nombre: {informacion_cliente['nombre']}\nEdad: {informacion_cliente['edad']}\nDirección: {informacion_cliente['direccion']}\nTeléfono: {informacion_cliente['telefono']}"

    return datos_usuario


def mostrar_datos_usuario_v2(informacion_cliente: dict) -> str:
    """
    Va mostrando datos del diccionario dependiendo de las claves que tenga el mismo.

    Args:
        informacion_cliente (dict): El diccionario con la información del cliente.

    Returns:
        str: La información del cliente formateada a cadena.
    """
    pass


def main():
    usuario = crear_diccionario()
    print(mostrar_datos_usuario(usuario))


if __name__ == "__main__":
    main()