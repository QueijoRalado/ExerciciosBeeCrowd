import random

numeroz = [-5,-4,-3, -2, -1, 0, 1, 2, 3, 4, 5]
escolhidos = []
n = 1

resultado=1
while resultado!=0:
    escolhidos = []
    for n in range(0,3):
        escolha = random.randint(0, 6)
        escolhidos.append(numeroz[escolha])
        print (escolhidos)

    resultado = escolhidos[0] + escolhidos[1] + escolhidos[2]
    print("---------------------------------------------------")

print (f"{escolhidos[0]} + {escolhidos[1]} + {escolhidos[2]} = {resultado}")
print("Os números escolhidos CONSEGUIRAM chegar no resultado correto!!!!")