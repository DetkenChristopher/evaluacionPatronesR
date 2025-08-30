
# 1. Máximo Común Divisor (MCD) 

#Algoritmo de Euclides
def mcd_recursivo(a, b):
    if b == 0:
        return a
    return mcd_recursivo(b, a % b)

#Iterativa
def mcd_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 2. Conteo en Lista Anidada 

# Recursiva
def contar_recursivo(lista):
    if lista == []:
        return 0
    primero, *resto = lista
    if isinstance(primero, list):
        return contar_recursivo(primero) + contar_recursivo(resto)
    else:
        return 1 + contar_recursivo(resto)

# Iterativa 
def contar_iterativo(lista):
    pila = [lista]
    contador = 0
    while pila:
        actual = pila.pop()
        for elem in actual:
            if isinstance(elem, list):
                pila.append(elem)
            else:
                contador += 1
    return contador



print("Pruebas MCD")
print("MCD Recursivo (48, 18):", mcd_recursivo(48, 18))
print("MCD Iterativo (48, 18):", mcd_iterativo(48, 18))

print("\n Pruebas Conteo Lista Anidada")
lista_prueba = [1, [2, [3, 4], 5], 6, [7, 8]]
print("Conteo Recursivo:", contar_recursivo(lista_prueba))
print("Conteo Iterativo:", contar_iterativo(lista_prueba))
