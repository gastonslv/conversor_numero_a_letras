from f_cargarDatos import cargarDato
from f_convertir import convertir
from f_ordenarDatos import ordenarPosiciones, asignarUnidades
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
unidades, millares, millones = asignarUnidades(numero)

print(millones, millares, unidades)
