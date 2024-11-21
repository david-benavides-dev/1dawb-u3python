# Ejercicio 3.1.7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.


abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


# Segundo intento, removiendo elementos de la lista original
def remover_multiplos_tres(abecedario: list) -> list:
    """
    
    """
    abecedario_sin_letras = []

 
    i = 0
    while i < len(abecedario):
        if i % 3 != 0:
            abecedario_sin_letras.append(abecedario[i - 1])


        i += 1

    return abecedario_sin_letras


def main():
    print(remover_multiplos_tres(abecedario))


if __name__ == "__main__":
    main()