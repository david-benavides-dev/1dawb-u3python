# Ejercicio 3.1.10
# Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.


precios = [
    50,
    75,
    46,
    22,
    80,
    65,
    8
]

def retornar_min_max(precios: list) -> list:
    """
    Calcula el precio menor y mayor de una lista dada y retorna una lista con los dos valores.

    Args:
        precios (list): Una lista con los números
    
    Returns:
        list: El precio mínimo y máximo en una lista.
    """
    minimo = min(precios)
    maximo = max(precios)

    return minimo, maximo


def mostrar_precios(precios: list) -> str:
    """
    Args:
        precios (list):
    
    Returns:
        str: Una cadena con el precio mínimo y máximo junto a un texto.
    """
    

    return f" {" ".join(map(str, precios))}"

def main():
    minmax = retornar_min_max(precios)

    print(mostrar_precios(minmax))


if __name__ == "__main__":
    main()