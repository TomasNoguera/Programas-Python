#for numeros_pares in range(1, 101):
    #if numeros_pares & 2 == 0:
        #print(numeros_pares)

suma_pares = 0
suma_impares = 0
m = 1
n = 5
 
for i in range(m, n +1):
  if i % 2 == 0:
    suma_pares += i
  else:
    suma_impares += i

print('La suma de los pares es ',suma_pares)
print('La suma de los impares es ',suma_impares)
