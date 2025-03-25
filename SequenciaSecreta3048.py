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
        numero_adiante=-2
    print(f"{numeros[numero_atras]}, atras")
    print(f"                 {numero}")
    print(f"                          {numeros[numero_adiante]} adiante")
    print(numeros[numero_atras]==numero and numeros[numero_adiante]==numeros[numero_atras])
    if numeros[numero_atras]==numero_comum and numeros[numero_adiante]==numeros[numero_atras]:
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