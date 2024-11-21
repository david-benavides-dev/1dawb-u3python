# Ejercicio 3.1.13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.


def pedir_numero(msj: str) -> float:
    """
    Solicita al estudiante una entrada, validando que sea un número.

    Args:
        msj (str): Mensaje que se mostrará al solicitar el número.

    Returns:
        float: El número introducido, validado y convertido a float.
    """
    num = None
    while num is None:
        num = input(msj)
        if not validar_numero(num):
            num = None
        else:
            return float(num)


def validar_numero(num: str) -> bool:
    """
    Valida que la entrada sea un número tipo float y esté entre el rango de 0 a 10.

    Args:
        num (str): El número a validar.

    Returns:
        bool: True si es número válido, False en caso de no serlo.
    """
    try:
        num = float(num)
        if num >= 0 and num <= 10:
            return True
        else:
            raise Exception("*ERROR* La nota debe estar entre 0 y 10.")

    except ValueError:
        print("*ERROR* Debe ser un número.")
        return False
    except Exception as e:
        print(e)
        return False


def add_numeros_lista(msj: str) -> list:
    """
    
    """
    lista_numeros = []

    salir = False
    while not salir:
        numero = pedir_numero(msj)
        if numero != "":
            lista_numeros.append(numero)
        else:
            salir = True
    
    return lista_numeros
            
        

def main():
    lista_de_numeros = add_numeros_lista("Introduce números: ")
    print(lista_de_numeros)


if __name__ == "__main__":
    main()