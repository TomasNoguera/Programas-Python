import random,os
import numpy as np

def escribir():
    sucursal = np.array([1,2,3,4,5])
    reporte_sucursal = open("reporte_sueldo_sucursal.txt","w")
    
    for c in range(5):
        reporte = sucursal[c]
        for i in range(random.randint(5,10)):
            codigo_empleado = random.randint(100,200)
            sueldo_empleado = random.randint(30000,50000)
            linea=str(codigo_empleado)+','+ str(reporte)+',' + str(sueldo_empleado)+ '\n'
            reporte_sucursal.write(linea)

    reporte_sucursal.close()

def corte_control():
    reporte_sucursal = open("reporte_sueldo_sucursal.txt","r")
    # leo una línea antes de entrar y cargo las variables
    linea=reporte_sucursal.readline().strip()  # Uso strip para quitar el fin de linea \n
    s=linea.split(',') # divido la línea leida usando el separador coma
    reporte=int(s[1])

    while linea != "":
        suma_sueldo = 0
        reporte_ant = reporte   
        while linea !="" and reporte == reporte_ant:
            codigo_empleado = int(s[0])
            sueldo_empleado = int(s[2])
            suma_sueldo += sueldo_empleado
            # Muestro
            print(f'{" "*12} {reporte:>8} Codigo empleado:{codigo_empleado:>8} Sueldo empleado:{sueldo_empleado:>8} ') # Muestro lo leido
            linea=reporte_sucursal.readline().strip() # Leo una nueva línea y cargo las variables
            if linea!='':
                s=linea.split(',') # divido la línea leida usando el separador coma
                reporte=int(s[1])     # Tomo reporte para cargar comparar con reporte anterior
        
        total_sucursal = suma_sueldo
        print(f'{" "*25} Total Sucursal: {total_sucursal:>4} ')
        
    reporte_sucursal.close()

if not os.path.exists('reporte_sueldo_sucursal.txt'):
    print(' '*12,'El archivo con los datos No Existe')
    print(' '*12,'Lo crearemos')
    escribir()
    print(' '*18,'Ya Cree el archivo')
    input('Presione Enter para continuar')

corte_control()