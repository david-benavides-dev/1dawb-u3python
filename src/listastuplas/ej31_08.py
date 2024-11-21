# Ejercicio 3.1.8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


def comprobar_palidromo(palabra):
    """
    
    """
    if palabra[::-1] == palabra:
        return True
    else:
        return False


def main():
    print(comprobar_palidromo("somos"))


if __name__ == "__main__":
    main()