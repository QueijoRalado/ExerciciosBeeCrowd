numeros = [1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1]
numeros2 = [5, 1, 1, 1, 2, 1]
numeros3 = [12, 1, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1]
numeros4 = [3, 1, 2, 1]
numero_atras = -1
numero_comum = 0
numero_adiante = 1
marcados=0
for numero in numeros:
    if numero_adiante==len(numeros):
        numero_adiante=-1
    print(f"{numeros[numero_atras]} - atras")
    print(f"                 {numero} - atual")
    print(f"                              {numeros[numero_adiante]} - adiante")
    if numero==numeros[numero_atras] and numero==numeros[numero_adiante]:
        numeros[numero_adiante-1] = f"({numero})"
        marcados+=1
        print("PASSEI SEGUNDO!!!")
    if numero!=numeros[numero_adiante]:
        numeros[numero_adiante-1] = f"({numero})"
        marcados+=1
        print("PASSEI PRIMEIRO!!!")
    numero_adiante+=1
    numero_atras+=1
for numero in numeros:
    print(numero)
print(marcados)