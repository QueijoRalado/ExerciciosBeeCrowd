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
#binariox_incompletos = []
#binariox_falso = []
#binariox = []
# aqui eu peço os números, simples
for n in range(1, 3):
    numero = int(input(f"Escreva o número desejado para a adição: [{n}º Número]\n"))
    numerox.append(numero)

# aqui eu transformo o número em binário e divido o conjunto dele entre a lista pra depois apagar as informações que não importam (o "0b")
for n in range(0,2):
    binariox_incompletos = []
    binariox_falso = []
    binariox = []
    numero = (bin(numerox[n]))
    for letra in numero:
        binariox_incompletos.append(letra)
# aqui eu apago as informações que não poderiam importar menos pra fazer a conta binária final (o "0b" no começo quando eu transformo o número inteiro em binário)
    for letra in range(0,2):
        binariox_incompletos.pop(0)

# definindo um limitador pro método abaixo
    delimitador = ""
# aqui eu converto os números separados da lista em uma string, juntando tudo e formando uma string completa só com os números
    binariox_falso = map(str, binariox_incompletos)
    binariox = delimitador.join(binariox_falso)
# aqui eu só transformo a variável "binariox" em int de novo para que eu possa fazer a conta final
    binariox = int(binariox)
    print(binariox)
    resultado = resultado+binariox
# NÃO FAZ NADA A PARTIR DAQUI SE NÃO TIVER O
# aqui eu vou pegar o resultado dos números em formato binário e criar uma variável em string para que eu ppssa fazer um processo abaixo

resultado_str = str(resultado)
resultado_real_caralho = []

# aqui eu reviso número por número e vejo qual é maior que 1, se for maior que um, vira zero, se não, ele só é appendado pra lista "resultado_real_caralho" normalmente
for letra_fodida in resultado_str:
    letra_fodida=int(letra_fodida)
    if letra_fodida>1:
        resultado_real_caralho.append(0)
    else:
        resultado_real_caralho.append(letra_fodida)

# aqui eu faço o mesmo processo de antes que me levava a colocar os itens separados em uma lista num string com todas juntas 
resultado_str = map(str, resultado_real_caralho)
resultado = delimitador.join(resultado_str)

# aqui eu só transformo o número binário em um número inteiro para mostrar no final
print(int(f"0b{resultado}", 2))