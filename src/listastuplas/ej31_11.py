# Ejercicio 3.1.11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.


def producto_escalar(v1: tuple, v2: tuple) -> int:
    """
    
    """
    producto = 0

    for i in range (len(v2)):
        producto += v1[i] * v2[i]

    return producto


def mostrar_resultado(v1: tuple, v2: tuple, resultado: int) -> str:
    """
    
    """
    resultado = "v1 = (" +  f"{', '.join(map(str, v1))}".rstrip() + ")\n" + "v2 = (" +  f"{', '.join(map(str, v2))}".rstrip() + ")\n" + f"Producto = {str(resultado)}"


    return resultado


def main():
    v1 = (1, 2, 3)
    v2 = (-1, 0, 2)

    resultado = producto_escalar(v1, v2)

    print(mostrar_resultado(v1, v2, resultado))


if __name__ == "__main__":
    main()