from f_cargarDatos import cargarDato
from f_convertir import convertir
from f_ordenarDatos import asignarUnidades
# Inicializacion variables globales
unidades = []
millares = []
millones = []

numero = 0
palabra_final = ''
entero = 0
decimal = 0

# MAIN
numero = cargarDato()

millones, millares, unidades  = asignarUnidades(numero)

palabra_final = convertir(millones, millares, unidades)

palabra_final = ' '.join(palabra_final.split())

print(palabra_final.capitalize())