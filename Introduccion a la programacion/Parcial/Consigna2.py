mayor_cantidad_paginas = 0
documento_mayor_paginas = ""
promedio_paginas = 0
total_paginas = 0
nombre_predeterminado = "No"

for i in range(1, 61):
    nombre_documento = (input(f"Ingrese el Nombre de su archivo({i} de 60): "))
    cantidad_paginas = int(input(f"Ingrese la Cantidad de paginas de su archivo({i} de 60): "))
    total_paginas = total_paginas + cantidad_paginas

    if cantidad_paginas > mayor_cantidad_paginas:
        mayor_cantidad_paginas = cantidad_paginas
        mayor_cantidad_paginas = i
        documento_mayor_paginas = nombre_documento
    if (nombre_documento == "Documento sin nombre.py"):
        nombre_predeterminado = "Si"
    
    promedio_paginas = total_paginas / 60

print(f"El nombre del archivo ingresado con mas paginas es: {documento_mayor_paginas}")
print(f"El promedio de paginas de los documentos ingresados es de: {promedio_paginas:.2}")
print(nombre_predeterminado)