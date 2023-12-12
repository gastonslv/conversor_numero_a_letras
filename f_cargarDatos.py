def cargarDato():
    num = 0
    decimal = 0
    bandera = False

    while not bandera:
        try:
            num = int(input("Ingrese el monto a convertir: "))
            decimal = int(input("Ingrese la parte decimal del monto (centavos): "))
        except ValueError:
            print("Valor invalido, por favor vuelva a intentarlo.")
            continue

        bandera = True
    return num, decimal

def descomponerNumero(numero):
    lista = []
    for i in numero:
        lista.append(i)
    return lista