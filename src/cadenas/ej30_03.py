# Ejercicio 3.0.3
# Tienes este código:
# palabra = 'banana'
# contador = 0
# for letra in palabra:
#     if letra == 'a':
#         contador = contador + 1
# print(contador)
# Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.


def cuenta(palabra, letra) -> int:
    """
    
    """
    contador = 0
    for letras in palabra:
        if letra in letras:
            contador = contador + 1

    return contador


def main():
    print(cuenta("banana", "a"))


if __name__ == "__main__":
    main()