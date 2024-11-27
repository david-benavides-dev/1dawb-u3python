# Ejercicio 3.1.13
# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.


def validar_numeros(num: str) -> bool:
    """
    Valida que la entrada sea un número tipo entero.

    Args:
        num (str): El número a validar.

    Returns:
        bool: True si es número válido, False en caso de no serlo.
    """
    try:
        int(num)
        return True

    except ValueError:
        return False


def validar_lista(lista: str) -> bool:
    """
    Valida que la cadena pasada por parámetros tenga comas y su contenido sean números.

    Args:
        lista (str): Una cadena de caracteres.
    
    Returns:
        bool: True si la cadena contiene solamente números y contiene comas, False en el caso contrario.
    """
    if "," not in lista:
        return False

    lista = lista.split(",")

    for numeros in lista:
        if not validar_numeros(numeros):
            return False
    return True


def pedir_numeros(msj: str) -> list:
    """
    Solicita al usuario una lista de números separados por comas, validando que sean números.

    Args:
        msj (str): Mensaje que se mostrará al solicitar los números

    Returns:
        list: Una lista con los números introducidos.
    """
    pedir_numeros = True

    while pedir_numeros:
        pedir_numeros = input(msj).strip()
    
        if not validar_lista(pedir_numeros):
            print("*ERROR* Debes introducir una lista de números separada por comas.")
            pedir_numeros = True
        else:
            lista_numeros = []
            pedir_numeros = pedir_numeros.split(",")

            for numero in pedir_numeros:
                lista_numeros.append(int(numero))

            return lista_numeros


def calcular_media(lista_numeros: list) -> list:
    """
    Calcula la media y de una lista de N números.

    Args:
        lista_numeros (list): La lista de números.

    Returns:
        int: La media.
    """
    media = 0

    for i in range(len(lista_numeros)):
        media += lista_numeros[i]

    media /= len(lista_numeros)

    return media


def calcular_desviacion_tipica(lista_numeros: list) -> int:
    """
    
    """
    n = 0
    xn = 0
    xi2n = 0
    varianza = 0

    # Calculo de N, XN y XI2N
    for i in range(len(lista_numeros)):
        n += lista_numeros[i]
        xn += (i+1) * lista_numeros[i]
        xi2n += ((i+1)*(i+1)) * lista_numeros[i]

    x = xn / n

    # Cálculo de varianza para hacer la desviación típica
    varianza = (xi2n / n) - (x**2)

    # Desviación típica = raiz de la varianza
    desviacion_tipica = varianza ** 0.5

    return round(desviacion_tipica, 3)


def mostrar_media_y_desviacio(media: int, desviacion_tipica: int) -> str:
    """
    
    """
    return f"MEDIA: {media}\nDESVIACION TIPICA: {desviacion_tipica}"


def main():
    numeros_lista = pedir_numeros("Introduce una lista de números (separados por coma) >> ")
    media = calcular_media(numeros_lista)
    desviacion_tipica = calcular_desviacion_tipica(numeros_lista)
    print(mostrar_media_y_desviacio(media, desviacion_tipica))

if __name__ == "__main__":
    main()