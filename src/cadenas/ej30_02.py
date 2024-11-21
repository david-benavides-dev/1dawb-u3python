# Ejercicio 3.0.2
# Dado que fruta es una variable de tipo cadena, ¿qué significa fruta[:]?


def main():
    fruta = "banana"

    print(fruta[:])

    print("""
          fruta[:] es la sintaxis de slice para cada uno de los elementos del string, sin especificar indice de inicio final.
          El formato de slicing consta de [inicio:fin:step]. Dado que no se indica ningún indice, lo único que haría sería
          crear una "copia" de la cadena.
          """)


if __name__ == "__main__":
    main()