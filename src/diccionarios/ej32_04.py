# Ejercicio 3.2.4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.


meses = {
    "01": "Enero",
    "02": "Febrero",
    "03": "Marzo",
    "04": "Abril",
    "05": "Mayo",
    "06": "Junio",
    "07": "Julio",
    "08": "Agosto",
    "09": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre",
}


def pedir_fecha(msj: str) -> list:
    """
    
    """
    fecha = input(msj)
    return fecha.split("/")


def mostrar_fecha(meses, fecha):
    """
    
    """
    mes = meses[fecha[1]]

    return f"{fecha[0]} de {mes} de {fecha[2]}"



def main():
    fecha = pedir_fecha("Dime la fecha con formato dd/mm/aaaa: ")

    print(mostrar_fecha(meses, fecha))


if __name__ == "__main__":
    main()