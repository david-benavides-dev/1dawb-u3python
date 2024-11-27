# Ejercicio 3.2.9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
def calcular_desviacion_tipica(lista_numeros: list) -> int:
    """
    
    """
    n = 0
    xn = 0
    xi2n = 0
    varianza = 0

    # Calculo de N y XN
    for i in range(len(lista_numeros)):

        xi2n += ((i+1)*(i+1)) * lista_numeros[i]

    # x = xn / n

    # varianza = (xi2n / n) - (x**2)


    return xi2n
def main():
    print(calcular_desviacion_tipica([3,5,8,1]))


if __name__ == "__main__":
    main()