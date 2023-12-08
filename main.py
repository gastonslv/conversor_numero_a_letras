from f_cargarDatos import cargarDato
from f_convertir import convertir
from f_ordenarDatos import ordenarPosiciones, asignarUnidades
# Inicializacion variables globales
unidades = 0
millares = 0
millones = 0

numero = 0
palabra_final = ''
entero = 0
decimal = 0

# MAIN
numero = cargarDato()
asignarUnidades(numero)

"""
palabra_final = convertir(numero)
print(palabra_final.capitalize())
"""