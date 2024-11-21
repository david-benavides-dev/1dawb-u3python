# Ejercicio 3.0.4
# Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método
# y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.


def cuenta(palabra, letra) -> int:
    """
    
    """
    return palabra.count(letra)


def main():
    print(cuenta("banana", "a"))


if __name__ == "__main__":
    main()