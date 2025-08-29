import random
import time



def seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

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




lista_original = [random.randint(0, 100000) for _ in range(20000)]


lista_sel = lista_original[:]
inicio = time.time()
seleccion(lista_sel)
t_sel = time.time() - inicio


lista_burb = lista_original[:]
inicio = time.time()
burbuja(lista_burb)
t_burb = time.time() - inicio


lista_merge = lista_original[:]
inicio = time.time()
merge_sort(lista_merge)
t_merge = time.time() - inicio



print("\nResultados de Tiempos:")
print(f"Selección: {t_sel:.4f} segundos")
print(f"Burbuja:   {t_burb:.4f} segundos")
print(f"MergeSort: {t_merge:.4f} segundos")
