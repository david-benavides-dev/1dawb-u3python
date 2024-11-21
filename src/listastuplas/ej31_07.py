# Ejercicio 3.1.7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.


abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


# Primer intento, creando y actualizando una lista nueva
def remover_multiplos_tres(abecedario):
    """
    
    """
    abecedario_sin_letras = []

    for letra in abecedario:
        if abecedario.index(letra) % 3 != 0:
            abecedario_sin_letras.append(letra)

    return abecedario_sin_letras


# Segundo intento, removiendo elementos de la lista original
def remover_multiplos_tres_v2(abecedario):
    """
    
    """
    i = len(abecedario)

    while i >= 0:
        if i % 3 == 0:
            abecedario.pop(i)

        i -= 1

    return abecedario


def main():
    print(remover_multiplos_tres(abecedario))
    print(remover_multiplos_tres_v2(abecedario))


if __name__ == "__main__":
    main()