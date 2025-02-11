matrix = [
    [1, 2, 3, 4],
    [4, 2, 6, 9],
    [7, 0, 4, 6],
    [1, 2, 3, 6]
]
n_linha = -1
n_coluna = -1
linha_total = 0

# isso aqui é pra definir o máximo das linha, é tipo fazer um len(linha) tlgd
for linha in matrix:
    linha_total+=1
print(linha_total)
# isso aqui é pro codigo saber onde o "0" está localizado, pra assim ele saber onde colocar os "0"s
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

# isso aqui é pro programa substituir os números da linha de onde o "0" está
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