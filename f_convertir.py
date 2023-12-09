def buscarPalabra(lista, largo, tipo):
    
    fragmento_palabra = ''
    
    unidades = []

    unidad = {
      "1": 'uno',
      "2": 'dos',
      "3": 'tres',
      "4": 'cuatro',
      "5": 'cinco',
      "6": 'sies',
      "7": 'siete',
      "8": 'ocho',
      "9": 'nueve'
    }
    unidadesOrdinales = {
      "11": 'once',
      "12": 'doce',
      "13": 'trece',
      "14": 'catorce',
      "15": 'quince',
      "16": 'dieciseis',
      "17": 'diecisiete',
      "18": 'dieciocho',
      "19": 'diecinueve'
    }
    decena = {
      "1": 'diez',
      "2": 'veinte',
      "3": 'treinta',
      "4": 'cuarenta',
      "5": 'cincuenta',
      "6": 'sesenta',
      "7": 'setenta',
      "8": 'ochenta',
      "9": 'noventa'
    }
    centena = {
      "1": 'cien',
      "2": 'doscientos',
      "3": 'trescientos',
      "4": 'cuatrocientos',
      "5": 'quinientos',
      "6": 'seiscientos',
      "7": 'setecientos',
      "8": 'ochocientos',
      "9": 'novecientos'
    }
    
    unidades.append(centena)             # 0
    unidades.append(decena)              # 1
    unidades.append(unidad)              # 2
    unidades.append(unidadesOrdinales)   # 3

    if largo == 3:
        for i in range(3):
            for key, value in unidades[i].items():

                ordinales = ['11','12','13', '14','15','16','17','18','19']
                if i == 1 and ((lista[1]+lista[2]) in ordinales):
                    for key, value in unidades[3].items():
                        if key == (lista[1]+lista[2]):
                            fragmento_palabra += value
                            break
                
                if key == lista[i]:
                    fragmento_palabra += value
    elif largo == 2:
        for i in range(1, 3):
            for key, value in unidades[i].items():

                ordinales = ['11','12','13', '14','15','16','17','18','19']
                if i == 1 and ((lista[1]+lista[2]) in ordinales):
                    for key, value in unidades[3].items():
                        if key == (lista[1]+lista[2]):
                            fragmento_palabra += value
                            break
                
                if key == lista[i]:
                    fragmento_palabra += value
    elif largo == 1:
        for key, value in unidades[2].items():   
                if key == lista[0]:
                    fragmento_palabra += value
    
    ###
    
    if tipo == 'millon':
        fragmento_palabra += ' millones '
    elif tipo == 'mil':
        fragmento_palabra += ' miles '
    elif tipo == 'unidad':
        pass

    return fragmento_palabra

def convertir(u_millon, u_mil, unidad):

    palabra = ''

    # unidad de millon
    if not u_millon:
        pass
    else:
        palabra += buscarPalabra(u_millon, len(u_millon), 'millon')

    # unidad de mil
    if not u_mil:
        pass
    else:
        palabra += buscarPalabra(u_mil, len(u_mil), 'mil')

    # unidad
    if not unidad:
        print("No se ingreso ningun numero")
        pass
    else:
        palabra += buscarPalabra(unidad, len(unidad), 'unidad')

    return palabra
    

"""
    while not salir:
      for i in range(len(numero)):
        if i == 0:
          for key, value in centena.items():
            if key[0] == numero[i]:
              palabra += value + " "
              break
        elif i == 1:
          for key, value in decena.items():
            if key[0] == numero[i]:
              if numero[i+1] == '0':
                palabra += value
              else:
                palabra += value + ' y '
              break
        elif i == 2:
          for key, value in unidad.items():
            if key[0] == numero[i]:
              palabra += value
              break
      salir = True
"""