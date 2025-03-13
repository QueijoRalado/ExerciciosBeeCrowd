'''
6+9=15 parece ok. Mas como pode estar certo 4+6=2?

Veja só. Mofiz trabalhou duro durante seu curso de Eletrônica Digital, mas quando lhe foi solicitado que implementasse um somador de 32 bits como exame no laboratório, ele acabou 
fazendo algum erro na parte de projeto. Depois de vasculhar seu projeto por uma hora e meia, ele encontrou seu erro. Ele estava fazendo soma de bits, mas seu carregador de bit 
(carry) sempre apresentava como saída o valor zero. Portanto,

4  = 00000000 00000000 00000000 00000100
+6 = 00000000 00000000 00000000 00000110
----------------------------------------
2  = 00000000 00000000 00000000 00000010


Claro que já é uma boa coisa ele finalmente ter encontrado o seu erro, mas isso foi muito tarde. Considerando seu esforço durante o curso, o instrutor deu a ele mais uma chance: 
Mofiz teria que escrever um programa eficiente que pegaria 2 valores decimais de 32 bits sem sinal como entrada e deveria produzir um número de 32 bits sem sinal como saída, ou 
seja, somando do mesmo modo como o circuito faz.
'''
resultado = 0
numerox = []
for n in range(1, 3):
    numero = int(input(f"Escreva o número desejado para a adição: [{n}º Número]\n"))
    numerox.append(numero)


for n in range(0,2):
    binariox_incompletos = []
    binariox_falso = []
    binariox = []
    numero = (bin(numerox[n]))
    for letra in numero:
        binariox_incompletos.append(letra)

    for letra in range(0,2):
        binariox_incompletos.pop(0)

    delimitador = ""
    binariox_falso = map(str, binariox_incompletos)
    binariox = delimitador.join(binariox_falso)
    binariox = int(binariox)
    print(binariox)
    resultado = resultado+binariox

resultado_str = str(resultado)
resultado_real_caralho = []

for letra_fodida in resultado_str:
    letra_fodida=int(letra_fodida)
    if letra_fodida>1:
        resultado_real_caralho.append(0)
    else:
        resultado_real_caralho.append(letra_fodida)

resultado_str = map(str, resultado_real_caralho)
resultado = delimitador.join(resultado_str)

print(int(f"0b{resultado}", 2))