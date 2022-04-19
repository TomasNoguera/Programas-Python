#from os import close
import random 
import numpy as np

def escribir():
    precipitaciones_sep = open("lluvias.txt","w")
    dia = 0

    for i in range(30):
        dia = i + 1
        mes = "09"
        anio = 2021
        precipitaciones = random.randint(0,200)
        linea= str(dia)+','+ str(mes)+','+ str(anio)+','+ str(precipitaciones) + '\n'
        precipitaciones_sep.write(linea) # Escribo en el archivo toda la línea

    precipitaciones_sep.close()

def informe_lluvias():    
    datos_precipitaciones = open("lluvias.txt","r")
    linea = datos_precipitaciones.readline().strip()
    print("PRECIPITACION SEPTIEMBRE:")
    print("")

    sin_lluvia = 0
    menor_milimetros = 0
    mayor_milimetros = 0
    
    while linea != '':
        s=linea.split(',') # Divide la línea leida usando el separador coma
        dia = (s[0])
        mes = (s[1])
        anio = int(s[2])
        precipitaciones = int(s[3])

        if precipitaciones >= 50:
            mayor_milimetros += 1
        
        elif precipitaciones < 50:
            menor_milimetros += 1
        
        elif precipitaciones == 0:
            sin_lluvia += 1

        linea = datos_precipitaciones.readline().strip() # Lee una nueva línea

    datos_precipitaciones.close()
    print(f"Días sin lluvia: {sin_lluvia}")
    print(f"Días con lluvia mayor a 50mm: {mayor_milimetros}")
    print(f"Días con lluvia menor a 50mm: {menor_milimetros}")

escribir()
informe_lluvias()