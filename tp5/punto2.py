# En una estación meteorológica se registra diariamente la temperatura máxima y mínima de todo un año con el siguiente diseño:
# Día-Mes-Anio-Temperatura_Maxima-Temperatura_Minima (éstos dos últimos se pueden generar aleatoriamente).
# Preparar un algoritmo con los procedimientos necesarios para: 
# a) cargar los datos correspondientes a todos los días del corriente año en un archivo llamado “ temperaturas.txt”. 
# b) imprima por pantalla un reporte como el siguiente: 
# TEMPERATURA: INFORME ANUAL  
# Temperatura Mínima Del Año: xx 
# Registrada el Día: xx 
# Del Mes: xx 
# Temperatura Máxima Del Año: xx 
# Registrada el Día: xx 
# Del Mes: xx 
# Máxima Amplitud Térmica: xx  
# Registrada el Día: xx  
# Del Mes: xx  


# Programas Accesorios:

def temperaturas_año_2021():
    # a) cargar los datos correspondientes a todos los días del corriente año en un archivo llamado “ temperaturas.txt”.
    temp_2021 = open("temperaturas.txt","w")
    mes = 0
    mes_largo = 31
    mes_medio = 30
    mes_corto = 28
    for i in range (12):
        mes = i + 1
        año = 2021
        if mes == 1 or mes == 3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes == 12:
            for x in range (mes_largo):
                dia = x + 1
                temp_max = random.randint(19,33)
                temp_min = random.randint(1,18)
                linea = str(dia)+","+ str(mes)+","+ str(año)+","+str(temp_max)+","+str(temp_min)+"\n"
                temp_2021.write(linea)
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            for x in range (mes_medio):
                dia = x + 1
                temp_max = random.randint(19,33)
                temp_min = random.randint(1,18)
                linea = str(dia)+","+ str(mes)+","+ str(año)+","+str(temp_max)+","+str(temp_min)+"\n"
                temp_2021.write(linea)
        else: 
            for x in range (mes_corto):
                dia = x + 1
                temp_max = random.randint(19,33)
                temp_min = random.randint(1,18)
                linea = str(dia)+","+ str(mes)+","+ str(año)+","+str(temp_max)+","+str(temp_min)+"\n"
                temp_2021.write(linea)  
    temp_2021.close()


def informe_anual_2021():
    # TEMPERATURA: INFORME ANUAL  
    # Temperatura Mínima Del Año: xx 
    # Registrada el Día: xx 
    # Del Mes: xx 
    # Temperatura Máxima Del Año: xx 
    # Registrada el Día: xx 
    # Del Mes: xx 
    # Máxima Amplitud Térmica: xx  
    # Registrada el Día: xx  
    # Del Mes: xx
    max_temp = 0
    max_dia = 0
    max_mes = 0
    min_temp = 1000
    min_dia = 0
    min_mes = 0 

    print()
    datos_temperaturas = open("temperaturas.txt","r")
    linea = datos_temperaturas.readline().strip()
    print("TEMPERATURA: INFORME ANUAL")

    while linea != '':
        s = linea.split(",")
        dia = int(s[0])
        mes = int(s[1])
        año = int(s[2])
        max = float(s[3])
        min = float(s[4])

        if max > max_temp:
            max_temp = max
            max_dia = dia
            max_mes = mes

        if min < min_temp:
            min_temp = min
            min_dia = dia
            min_mes = mes

        linea = datos_temperaturas.readline().strip()

    datos_temperaturas.close()
    print(f"Temperatura Mínima Del Año: {min_temp}.\nRegistrada el Día: {min_dia}\nDel Mes:  {min_mes}")
    print()
    print(f"Temperatura Máxima Del Año:  {max_temp}.\nRegistrada el Día: {max_dia}\nDel Mes: {max_mes}")
    




# Programa Principal:

import random
from pyrecord import Record

temperaturas_año_2021()
informe_anual_2021()