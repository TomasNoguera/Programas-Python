def sumatoria(n):
    suma = 0
    
    for i in range(1, n+1):
        suma = suma + i
    return suma

print(sumatoria(50))