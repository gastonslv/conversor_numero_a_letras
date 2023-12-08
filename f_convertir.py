def convertir(numero):

  numero = str(numero)

  salir = False

  palabra = ''
  
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
  postUnidadPreDecena = {
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
    "10": 'diez',
    "20": 'veinte',
    "30": 'treinta',
    "40": 'cuarenta',
    "50": 'cincuenta',
    "60": 'sesenta',
    "70": 'setenta',
    "80": 'ochenta',
    "90": 'noventa'
  }
  centena = {
    "100": 'cien',
    "200": 'doscientos',
    "300": 'trescientos',
    "400": 'cuatrocientos',
    "500": 'quinientos',
    "600": 'seiscientos',
    "700": 'setecientos',
    "800": 'ochocientos',
    "900": 'novecientos'
  }

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
  return palabra