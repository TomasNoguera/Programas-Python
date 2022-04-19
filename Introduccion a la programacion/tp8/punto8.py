"""
Ingresa los mililitros de lluvia caídos diariamente en una semana y informa en pantalla el promedio de precipitaciónes de 
esa semana.
"""

#Cantidad de lluvia caida en la semana
lluvia_semanal = 0
#Por si no ha llovido
dia_mas_lluvio = "- (No ha llovido esta semana)"
# Variable auxiliar
mayor_lluvia = 0

for dia in ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado']:
    lluvia_dia = int(input(f"Ingrese cuantos mililitros han caido el día {dia}: "))
    if lluvia_dia > mayor_lluvia:      
        dia_mas_lluvio = dia
        mayor_lluvia = lluvia_dia
    lluvia_semanal += mayor_lluvia

#Calculamos el promedio dividiendo la cantidad de mililitros caidos en la semana por la cantidad de dias (7)    
promedio_semanal = lluvia_semanal / 7

print(f"El promedio de precipitaciones fue de {promedio_semanal:.2} mls. diarios.") # "":.2" Hace que solo tome 2 valores.
print(f"El día de más precipitaciones fue el {dia_mas_lluvio}.")