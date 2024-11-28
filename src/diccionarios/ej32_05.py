# Ejercicio 3.2.5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después 
# muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.


asignaturas =  {'Matemáticas': 6,
                'Física': 4,
                'Química': 5
                } 


def sumar_creditos(asignaturas: dict) -> int:
    """
    Suma las llaves enteras de un diccionario clave-valor.

    Args:
        asignaturas (dict): El diccionario.

    Returns:
        creditos (int): La sumatoria de las claves del diccionario.
    """
    creditos = 0

    for asignatura in asignaturas:
        creditos += asignaturas[asignatura]
    
    return creditos


def mostrar_asignaturas_creditos(asignaturas: dict) -> str:
    """
    Muestra el diccionario de forma ordenada junto a sus claves y la sumatoria de todas las claves del mismo.

    Args:
        asignaturas (dict): Diccionario de las asignaturas a mostrar.

    Returns:
        string_asignaturas (str): Cadena con las asignaturas ordenadas y la sumatoria de los valores de las mismas.
    """
    string_asignaturas = ""
    creditos_totales = sumar_creditos(asignaturas)

    for asignatura in asignaturas:
        string_asignaturas += f"{asignatura} tiene {asignaturas[asignatura]} créditos.\n"

    string_asignaturas += f"Creditos totales del curso: {creditos_totales}."
    
    return string_asignaturas


def main():
    print(mostrar_asignaturas_creditos(asignaturas))


if __name__ == "__main__":
    main()