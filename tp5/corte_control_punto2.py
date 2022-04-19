import random,os
import numpy as np

def escribir():
    sucursal = np.array([1,2,3,4,5])
    reporte_sucursal = open("reporte_sueldo_departamento.txt","w")
    
    for c in range(5):
        reporte = sucursal[c]
        for i in range(random.randint(5,10)):
            codigo_empleado = random.randint(100,200)
            codigo_departamento = random.randint(1,10)
            sueldo_empleado = random.randint(30000,50000)
            linea=str(codigo_empleado)+','+ str(codigo_departamento)+','+ str(reporte)+',' + str(sueldo_empleado)+ '\n'
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
        total_departamento = 0
        total_sucursal = 0
        reporte_ant = reporte   
        
        while linea !="" and reporte == reporte_ant:
            codigo_empleado = int(s[0])
            sueldo_empleado = int(s[2])
            codigo_departamento = int(s[3])
            
            suma_sueldo += sueldo_empleado
            total_sucursal = suma_sueldo
            # Muestro
            print(f'{" "*12} Departamento: {codigo_departamento:>8} Codigo empleado:{codigo_empleado:>8} Sueldo empleado:{sueldo_empleado:>8} ')
            linea=reporte_sucursal.readline().strip()
            
            if codigo_departamento == int(s[3]):
                total_departamento += sueldo_empleado
                linea=reporte_sucursal.readline().strip()
            #print(f'{" "*12} Departamento: {codigo_departamento:>8} total departamento: {total_departamento:>8}')
            codigo_departamento = int(s[3])
            
            if reporte == int(s[1]):
                total_sucursal += total_departamento
                reporte=int(s[1])
                linea=reporte_sucursal.readline().strip()

            if linea!='':
                s=linea.split(',')
                reporte=int(s[1])
        
        #total_sucursal = suma_sueldo
        print(f'{" "*25} Total Separtamento: {total_departamento:>4}')
        print(f'{" "*25} Total Sucursal: {total_sucursal:>4} ')
        
    reporte_sucursal.close()

if not os.path.exists('reporte_sueldo_departamento.txt'):
    print(' '*12,'El archivo con los datos No Existe')
    print(' '*12,'Lo crearemos')
    escribir()
    print(' '*18,'Ya Cree el archivo')
    input('Presione Enter para continuar')

corte_control()

    # reporte_sucursal = open("reporte_sueldo_departamento.txt","r")
    # linea=reporte_sucursal.readline().strip()  # Uso strip para quitar el fin de linea \n
    # s=linea.split(',') # divido la línea leida usando el separador coma
    # reporte=int(s[0])
    # codigo_departamento = int(s[1])
    # codigo_empleado = int(s[2])
    # sueldo_empleado = int(s[3])
    
    # while linea != "":
    #     s=linea.split(',')
    #     total_sucursal = 0
    #     while linea !="" and reporte == int(s[0]):
    #         s=linea.split(",")
    #         total_departamento = 0
    #         while codigo_departamento == int(s[1]) and linea !="":
    #             s=linea.split(",")
    #             sueldo_empleado = int(s[3])
    #             if codigo_departamento == int(s[1]):
    #                 total_departamento += sueldo_empleado
    #                 linea=reporte_sucursal.readline().strip()
    #         print(f'{" "*12} Departamento: {codigo_departamento} total departamento: {total_departamento}')
    #         codigo_departamento = int(s[1])
    #         if reporte == int(s[0]):
    #             total_sucursal += total_departamento
    #             reporte=int(s[0])
    #     print()
    #     print(f'{" "*12}Total Sucursal: {total_sucursal} Sucursal: {reporte}')
    #     print()
    #     reporte=int(s[0])