mayor = 0
promedio_lluvia = 0

for i in range (1, 8):
    numero_lluvia = int(input(f"Ingrese los militros caidos el dia {i} de la semana: "))
    lluvia_semanal = numero_lluvia + numero_lluvia
    if numero_lluvia > mayor:
        mayor = numero_lluvia
promedio_lluvia = lluvia_semanal / 7

print("El promedio de precipitaciones fue de ", promedio_lluvia,"Mls diarios.")
print("El dia de la semana con mas precipitaciones fue el dia ")