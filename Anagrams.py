'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

QueijoRalado falando, esse exercício foi um inferno na terra para terminar (não terminei ainda, apenas escrevei que "foi" pois eu vou terminar isso aqui na base do ódio)
'''

coisax = ["eat","tea","tan","ate","nat","bat"]
coisax2 = coisax.copy()

anagramas_falso = []
anagramas = []
anagramas_definitivo = []
checar_escolhida = sorted(coisax[0])
checagem = 0
cheio = False


n2=0
while len(coisax)!=0:
    n2=0
    palavra_escolhida = sorted(coisax[0])
    print("palavra escolhida", palavra_escolhida)
    while n2!=len(coisax):
        print("n2", n2)
        if palavra_escolhida==sorted(coisax[n2]):
            anagramas_falso.append(coisax[n2])
            coisax.pop(n2)
            n2-=1
            print("falso", anagramas_falso)
        n2+=1
        if (n2==len(coisax)):
            cheio=True

    if cheio:
        anagramas_definitivo.append(anagramas_falso)
    print("definitivo 1", anagramas_definitivo)
    while len(anagramas_falso)!=0:
        anagramas_falso.pop()
    print("definitivo 2", anagramas_definitivo)