import random
import numpy as np

def archivo1(cant): 
    # Creo una lista para las carreras y así cargar en el archivo
    clientes = open('clientes.dat','w') # Creo y Abro el archivo # Cargo una materia para grabar
    for i in range(cant): # Genero los registros de cada materia
        cuenta=i
        cliente=i+100
        saldo=random.randint(-2000,2000)
        linea= str(cuenta)+','+ str(cliente)+','+ str(saldo)+ '\n'
        clientes.write(linea) # Escribo en el archivo toda la línea 

    clientes.close()   

def archivo2(cant): 
  # Creo una lista para las carreras y así cargar en el archivo
  movimientos = open('movimientos.dat','w') # Creo y Abro el archivo # Cargo una materia para grabar
  i=0
  for i in range(cant):
      mov=random.randint(0,1)
      if mov==1:
        for j in range(random.randint(1,4)): # Genero los registros de cada materia
          cuenta=i
          movimiento=random.randint(1,2)
          importe=random.randint(1,2000)
          linea=str(cuenta)+','+ str(movimiento)+','+ str(importe)+ '\n'
          movimientos.write(linea) # Escribo en el archivo toda la línea
  movimientos.close()  

def clientes_activos():
  #Esta funcion compara los numeros de cuenta del primer archivo con los del segundo. Si hay una coincidencia,significa
  #que el cliente con ese numero de cuenta realizo algún movimiento bancario. Entonces paso numero de cuenta, cliente y saldo
  # a un nuevo archivo. Más abajo explico en mayor profuncidad.
  clientes=open("clientes.dat","r")
  movimientos=open("movimientos.dat","r")
  clientes_activos=open("clientesActivos.dat","w")
  linea=clientes.readline().strip() 
  s=linea.split(',')
  cuenta_ant=-1
  linea2="a"
  while linea!="" and linea2!="" :
    encontrado=False
    linea2=movimientos.readline().strip()
    a=linea2.split(",")
    while linea!="" and linea2!="" and encontrado==False: #mientras no haya encontrado una coincidencia y los archivos no terminen
      cuenta=int(s[0])
      cliente=int(s[1])
      saldo=int(s[2])
      cuenta_activa=int(a[0])
      if cuenta==cuenta_activa: #si encuentra coincidencia
        if cuenta!=cuenta_ant: #comparo para ver si este cliente no está guardado. Si lo esta, paso de largo y si no, escribo
          linea3= str(cuenta)+','+ str(cliente)+','+ str(saldo)+ '\n'
          clientes_activos.write(linea3)
          cuenta_ant=cuenta #cargo el valor de esta cuenta para que no se repita
        encontrado=True
      elif cuenta<cuenta_activa: # si el numero de cuenta de clientes es menor al de cuenta en movimientos, lo aumento
        linea=clientes.readline().strip() 
        s=linea.split(',')
      else:  # si el numero de cuenta de movimientos es menor al de cuenta en clientes, lo aumento
        linea2=clientes.readline().strip() 
        a=linea2.split(',')
      #de esta forma recorro los dos archivos
  clientes.close()
  movimientos.close()  
  clientes_activos.close()


def corte_control():
    clientes = open('clientesActivos.dat','r')
    movimientos=open("movimientos.dat","r")
    linea=clientes.readline().strip() 
    s=linea.split(',') 
    linea2=movimientos.readline().strip()
    a=linea2.split(",")
    cuenta=int(a[0])    
    while linea2!='': # cuando línea sea vacía '' finalizó el archivo
        cuenta_ant=cuenta
        saldo=int(s[2])
        while linea2!='' and cuenta==cuenta_ant:  
            #guardo datos
            movimiento=int(a[1])
            importe=int(a[2])
            cliente=int(s[1])
            if movimiento==1: #deposito
              saldo+=importe #sumo al saldo
            else: #extraccion
              saldo=saldo-importe  #resto al saldo
            linea2=movimientos.readline().strip()
            if linea2!='':
                a=linea2.split(',') 
                cuenta=int(a[0]) 
        print(f" Nro de cuenta: {cuenta_ant} Cliente: {cliente}  Saldo: {saldo}   ")
        linea=clientes.readline().strip()
        s=linea.split(",")       
    clientes.close() 
    movimientos.close() 
cant=10

archivo1(cant) #creo el primer archivo
archivo2(cant) #creo el segundo archivo con los movimientos
clientes_activos() #guardo en un nuevo archivo solamente los clientes que realizaron algun movimiento
corte_control()