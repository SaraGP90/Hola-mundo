def sumar_listas(lista1, lista2):
    # Verificar que ambas listas tengan la misma longitud
    if len(lista1) != len(lista2):
        return "Las listas deben tener la misma longitud"
    
    # Inicializar una lista para almacenar la suma de los elementos
    suma = []
    
    # Iterar sobre ambas listas y sumar los elementos correspondientes
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    
    return suma

# Ejemplo de uso
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7,
   def multiplicar_listas(lista1, lista2):
    # Verificar que ambas listas tengan la misma longitud
    if len(lista1) != len(lista2):
        return "Las listas deben tener la misma longitud"
    
    # Inicializar una lista para almacenar el resultado de la multiplicación
    resultado = []
    
    # Iterar sobre ambas listas y multiplicar los elementos correspondientes
    for i in range(len(lista1)):
        resultado.append(lista1[i] * lista2[i])
    
    return resultado

# Ejemplo de uso
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
resultado = multiplicar_listas(lista1, lista2)
print("Resultado de la multiplicación de las listas:", resultado)
       
