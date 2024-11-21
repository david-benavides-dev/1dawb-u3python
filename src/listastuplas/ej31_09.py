# Ejercicio 3.1.9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.


vocales = ["a","e","i","o","u"]


def contar_vocales(vocales: list, palabra: str) -> int:
    """
    
    """
    lista_vocales = []

    for vocal in vocales:
        lista_vocales.append(palabra.lower().count(vocal))

    return lista_vocales


def mostrar_vocales(lista_vocales: list):
    pass


def main():
    palabra = input(">> ")
    a,e,i,o,u = contar_vocales(vocales, palabra)

    print(f"En la palabra {palabra} aparece la a {a} veces, la e {e} veces, la i {i} veces, la o {o} veces y la u {u} veces.")


if __name__ == "__main__":
    main()