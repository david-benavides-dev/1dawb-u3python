# Ejercicio 3.2.3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
#
# Fruta 	Precio
# Plátano 	1.35
# Manzana 	0.80
# Pera 	    0.85
# Naranja 	0.70


Frutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}


def validar_num(num: str) -> bool:
    """
    
    """
    try:
        int(num)
        return True
    except ValueError:
        print("*ERROR* Debes introducir un número correcto.")
        return False


def calcular_precio_kg(fruta: int, kg: int) -> int:
    """
    
    """
    precio = Frutas[fruta] * kg
    return precio


def preguntar_fruta(msj: str) -> dict:
    """
    
    """
    preguntar_usuario = None

    while not preguntar_usuario:
        preguntar_usuario = input(msj).capitalize()
        if preguntar_usuario not in Frutas:
            preguntar_usuario = None

        else:

            return preguntar_usuario


def preguntar_kg(msj: str) -> int:
    """
    
    """
    preguntar_usuario = None

    while not preguntar_usuario:
        preguntar_usuario = input(msj)
        if not validar_num(preguntar_usuario):
            preguntar_usuario = None
        else:
            return int(preguntar_usuario)


def mostrar_precio_kg(fruta, kg):
    """
    
    """
    calcular_precio = calcular_precio_kg(fruta, kg)
    return f"Sus {kg} kilos de {fruta} cuestan {calcular_precio}."


def main():
    kg = preguntar_kg("Introduce la cantidad de kilos: ")
    fruta = preguntar_fruta("Introduce la fruta: ")
    print(mostrar_precio_kg(fruta, kg))


if __name__ == "__main__":
    main()