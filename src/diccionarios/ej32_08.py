# Ejercicio 3.2.8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá
# las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir.


def pedir_frase(msj):
    """
    
    """
    frase = input(msj)
    return frase


def generar_diccionario_ingles():
    """
    
    """
    traduccion = dict()

    validar_frase = False
    while not validar_frase:
        try:
            par_palabras = input("Introduce las palabras con el formato <palabra>:<traduccion>,<... (cada par separado por comas) >> ").strip()

            palabras_lista = par_palabras.split(",")

            if "," not in par_palabras:
                raise ValueError("Formato incorrecto")

            for palabra in palabras_lista:
                clave, valor = palabra.split(":")
                traduccion.update({clave: valor})

                validar_frase = True

        except ValueError as e:
            print(f"*ERROR*: {e}")
            validar_frase = False

    return traduccion


def traduccir_frase(diccionario: dict, frase: str) -> str:
    """
    
    """
    frase_traducida = ""

    palabras = frase.split(" ")

    for palabra in palabras:
        if palabra in diccionario.keys():
            frase_traducida += diccionario[palabra] + " "
        else:
            frase_traducida += palabra + " "
    
    return frase_traducida


def main():

    diccionario_ingles = generar_diccionario_ingles()

    frase = pedir_frase("Introduce una frase: ")

    frase_traducida = traduccir_frase(diccionario_ingles, frase)

    print(frase_traducida)


if __name__ == "__main__":
    main()