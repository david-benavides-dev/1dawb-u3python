# Ejercicio 3.1.6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


asignaturas = [
    "Matemáticas",
    "Física",
    "Qúimica",
    "Historia",
    "Lengua",
]


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


def remover_asignaturas(asignaturas: list) -> list:
    """
    
    """
    asignaturas_suspendidas = []

    for asignatura in asignaturas:
        nota_asignatura = pedir_numero(f"Introduzca su nota en {asignatura}: ")
        if nota_asignatura < 5:
            asignaturas_suspendidas.append(asignatura)

    return asignaturas_suspendidas


def mostrar_asignaturas_repetidas(asignaturas_estudiante: list) -> str:
    """
    
    """
    return f"Debes repetir {' '.join(map(str, asignaturas_estudiante))}"


def main():
    asignaturas_repetir = remover_asignaturas(asignaturas)
    print(mostrar_asignaturas_repetidas(asignaturas_repetir))


if __name__ == "__main__":
    main()