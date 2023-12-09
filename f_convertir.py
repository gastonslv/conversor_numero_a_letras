def armarPalabra(lista, largo, tipo, unidades):

    fragmento_palabra = ''

    if tipo == 'millon':
        if largo == 1:
            
            if lista[0] == '1': # excepcion
                fragmento_palabra += 'Un millon '
            
            else:
                for key, value in unidades[2].items():
                    if key == lista[0]:
                        fragmento_palabra += value
                
                fragmento_palabra += ' millones '
        
        elif largo == 2:
            
            if lista[0] == '1' and lista[1] != '0':
                # aplicamos las unidades ordinales

                for key, value in unidades[3].items():
                    if key == (lista[0] + lista[1]):
                        fragmento_palabra += value
                
                fragmento_palabra += ' millones '
            
            else:

                for i in range(2): # no hay centena
                    for key, value in unidades[i+1].items():
                        if key == lista[i]:
                            fragmento_palabra += value
                            if i == 0 and lista[1] != '0':
                                fragmento_palabra += ' y '
            
                fragmento_palabra += ' millones '

        elif largo == 3:

            for i in range(3):
                for key, value in unidades[i].items():
                    if key == lista[i]:
                        if i == 0 and lista[0] == '1' and lista[1] != '0': # si es en la primera vuelta
                            fragmento_palabra += ' ciento '
                        elif i == 1 and lista[1] == '1' and lista[2] != '0':
                            for key, value in unidades[3].items():
                                if key == (lista[1] + lista[2]):
                                    fragmento_palabra += value
                        else:
                            if i == 2 and lista[1] == '1' and lista[2] != '0': 
                                continue
                            else:
                                fragmento_palabra += ' ' + value + ' '
                                if i == 1 and lista[2] != '0':
                                    fragmento_palabra += ' y '

            fragmento_palabra += ' millones '  
    
    elif tipo == 'mil':
        if largo == 1:
            if lista[0] == '1':
                fragmento_palabra = ' mil '
            else:
                for key, value in unidades[2].items():
                    if key == lista[0]:
                        fragmento_palabra += value
                
                fragmento_palabra += ' mil '
        
        elif largo == 2:

            if lista[0] == '1' and lista[1] != '0':
                # aplicamos unidades ordinales
                for key, value in unidades[3].items():
                    if key == (lista[0] + lista[1]):
                        fragmento_palabra += value
                
                fragmento_palabra += ' mil '
        
            else:

                for i in range(2):
                    for key, value in unidades[i+1].items():
                        if key == lista[i]:
                            fragmento_palabra += value
                            if i == 0 and lista[1] != '0':
                                fragmento_palabra += ' y '
                
                fragmento_palabra += ' mil '
        
        elif largo == 3:

            for i in range(3):
                for key, value in unidades[i].items():
                    if key == lista[i]:
                        if i == 0 and lista[0] == '1' and lista[1] != '0': # si es en la primera vuelta
                            fragmento_palabra += ' ciento '
                        elif i == 1 and lista[1] == '1' and lista[2] != '0':
                            for key, value in unidades[3].items():
                                if key == (lista[1] + lista[2]):
                                    fragmento_palabra += value
                        else:
                            if i == 2 and lista[1] == '1' and lista[2] != '0': 
                                continue
                            else:
                                fragmento_palabra += ' ' + value + ' '
                                if i == 1 and lista[2] != '0':
                                    fragmento_palabra += ' y '
        
            fragmento_palabra += ' mil '

    elif tipo == 'unidad':
        if largo == 1:
            if lista[0] == '1':
                fragmento_palabra = ' mil '
            else:
                for key, value in unidades[2].items():
                    if key == lista[0]:
                        fragmento_palabra += value
        
        elif largo == 2:

            if lista[0] == '1' and lista[1] != '0':
                # aplicamos unidades ordinales
                for key, value in unidades[3].items():
                    if key == (lista[0] + lista[1]):
                        fragmento_palabra += value
        
            else:

                for i in range(2):
                    for key, value in unidades[i+1].items():
                        if key == lista[i]:
                            fragmento_palabra += value
                            if i == 0 and lista[1] != '0':
                                fragmento_palabra += ' y '
        
        elif largo == 3:

            for i in range(3):
                for key, value in unidades[i].items():
                    if key == lista[i]:
                        if i == 0 and lista[0] == '1' and lista[1] != '0': # si es en la primera vuelta
                            fragmento_palabra += ' ciento '
                        elif i == 1 and lista[1] == '1' and lista[2] != '0':
                            for key, value in unidades[3].items():
                                if key == (lista[1] + lista[2]):
                                    fragmento_palabra += value
                        else:
                            if i == 2 and lista[1] == '1' and lista[2] != '0': 
                                continue
                            else:
                                fragmento_palabra += ' ' + value + ' '
                                if i == 1 and lista[2] != '0':
                                    fragmento_palabra += ' y '
    
    return fragmento_palabra
    
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

    unidades.append(centena)             # 0
    unidades.append(decena)              # 1
    unidades.append(unidad)              # 2
    unidades.append(unidadesOrdinales)   # 3

    fragmento_palabra = armarPalabra(lista, largo, tipo, unidades)

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
