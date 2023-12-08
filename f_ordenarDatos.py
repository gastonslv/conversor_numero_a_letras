def ordenarPosiciones(lista):
    aux = ''
    digitos = len(lista)

    if not lista:
        pass
    else:
        if digitos == 1:
            pass
        elif digitos == 2:
            aux = lista[0]
            lista[0] = lista[1]
            lista[1] = aux
        elif digitos == 3:
            aux = lista[0]
            lista[0] = lista[2]
            lista[2] = aux
    return lista

def asignarUnidades(numeroDesc):
    numeroDesc = str(numeroDesc)
    unidades = 1 # 3 = unidad | 6 = miles | 9 = millones
    millon = []
    mil = []
    unidad = []

    for i in range(1, (len(numeroDesc) + 1)):
        i *= -1
        if unidades <= 3:
            unidad.append(numeroDesc[i])
        elif unidades >=4 and unidades <= 6:
            mil.append(numeroDesc[i])
        else:
            millon.append(numeroDesc[i])
        unidades += 1

    print(millon, mil, unidad) ## borrar

    unidad = ordenarPosiciones(unidad)
    mil = ordenarPosiciones(mil)
    millon = ordenarPosiciones(millon)

    return unidad, mil, millon