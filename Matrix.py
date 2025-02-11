'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]]
Output: [
    [1,0,1],
    [0,0,0],
    [1,0,1]]

Input: matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]]
Output: [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]]

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/



'''
matrix = [
    [0, 2, 9, 0],
    [4, 2, 6, 9],
    [7, 8, 4, 6],
    [1, 2, 3, 6]
]
n_linha = -1
n_coluna = -1
n_linha_seg_0 = -1
n_coluna_seg_0 = -1
linha_total = 0

# isso aqui é pra definir o máximo das linhas horizontais, é tipo fazer um len(linha) tlgd
for linha in matrix:
    linha_total+=1
# isso aqui é pro codigo saber onde o primeiro "0" está localizado, pra assim ele saber onde colocar os "0"s
for linha in matrix:
    n_linha+=1
    for numero in linha:
        n_coluna+=1
        if len(linha)<=n_coluna:
            n_coluna=0
        print(numero)
        if numero!=0:
            print ("não é 0")
        else:
            print("é 0")
            break
    if numero==0:
        break

matrix[n_linha][n_coluna] = 1 #<----- substituo o primeiro 0 por um número aleatorio para que assim o proximo for não encontre apenas o primeiro zero novamente

# codigo extra pro segundo "0"
for linha in matrix:
    n_linha_seg_0+=1
    for numero in linha:
        n_coluna_seg_0+=1
        if len(linha)<=n_coluna_seg_0:
            n_coluna_seg_0=0
        print(numero)
        if numero!=0:
            print ("não é 0")
        else:
            print("é 0")
            break
    if numero==0:
        break
# isso aqui é pro programa substituir os números da linha de onde o primeiro "0" está
n_coluna2 = 0
while len(linha)!=n_coluna2:
    matrix[n_linha][n_coluna2] = 0
    n_coluna2+=1
    for linha in matrix:
        print(linha)
    print("-----------")

n_linha2 = 0
while linha_total!=n_linha2:
    matrix[n_linha2][n_coluna] = 0
    n_linha2+=1
    for linha in matrix:
        print(linha)
    print("-----------")

# codigo extra pro segundo "0"

n_coluna2 = 0
while len(linha)!=n_coluna2:
    matrix[n_linha_seg_0][n_coluna2] = 0
    n_coluna2+=1
    for linha in matrix:
        print(linha)
    print("-----------")

n_linha2 = 0
while linha_total!=n_linha2:
    matrix[n_linha2][n_coluna_seg_0] = 0
    n_linha2+=1
    for linha in matrix:
        print(linha)
    print("-----------")