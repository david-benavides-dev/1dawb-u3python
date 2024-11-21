# Ejercicio 3.0.1
# Escribe un bucle while que comience con el último carácter en la cadena
# y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.


def recorrer_palabra_inversa(palabra: str) -> str:
    """
    
    """
    cont = 0

    palabra_inversa = ""

    while cont < len(palabra):
        palabra_inversa += "\n" + palabra[len(palabra)-cont-1]
        cont += 1

    return palabra_inversa.lstrip()


def main():
    print( recorrer_palabra_inversa("hola"))


if __name__ == "__main__":
    main()