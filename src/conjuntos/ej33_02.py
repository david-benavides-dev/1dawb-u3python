# Ejercicio 3.3.2
# Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, 
# finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.
#     Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
#     Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
#     Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
#     Mostrar si todos los nombres de primaria están incluidos en secundaria.


def solicitar_nombres_primaria():
    nombres_primaria = set()

    salir_bucle = False
    while not salir_bucle:
        nombres = input("Intoduce un nombre >> ")
        if nombres == "x":
            salir_bucle = True
        else:
            nombres_primaria.add(nombres)
    
    return nombres_primaria


def solicitar_nombres_secundaria():
    nombres_secundaria = set()

    salir_bucle = False
    while not salir_bucle:
        nombres = input("Intoduce un nombre >> ")
        if nombres == "x":
            salir_bucle = True
        else:
            nombres_secundaria.add(nombres)
    
    return nombres_secundaria


def main():
    primaria = solicitar_nombres_primaria()
    secundaria = solicitar_nombres_secundaria()
    print(primaria)
    print(secundaria)


if __name__ == "__main__":
    main()