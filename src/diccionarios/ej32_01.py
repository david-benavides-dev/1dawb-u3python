# Ejercicio 3.2.1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.


monedas = {
    "Euro": "€",
    "Yen": "¥",
    "Dollar": "$",
}


def preguntar_divisa(msj):
    """
    
    """
    preguntar_usuario = None
    while preguntar_usuario is None:
        preguntar_usuario = input(msj).capitalize()
        if preguntar_usuario not in monedas:
            print("Esa moneda no se encuentra en el diccionario.")
            preguntar_usuario = None
        else:
            return monedas[preguntar_usuario]


def main():
    print(preguntar_divisa("Dime la divisa: "))


if __name__ == "__main__":
    main()