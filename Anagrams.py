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
'''

coisax = ["eat","tea","tan","ate","nat","bat"]
anagramas_falso = []
anagramas = []
anagramas_definitivo = []
checar_escolhida = sorted(coisax[0])

n2=0
while len(coisax)!=0:
    n2=0
    palavra_escolhida = sorted(coisax[0])
    for n in range (len(coisax)):
        while n2!=len(coisax):
            if palavra_escolhida==sorted(coisax[n2]):
                anagramas_falso.append(coisax[n2])
                coisax.pop(n2)
                n2-=1
            n2+=1
anagramas_definitivo.append(anagramas_falso)
print(anagramas_definitivo)