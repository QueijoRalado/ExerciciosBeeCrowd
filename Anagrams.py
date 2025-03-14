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

coisax_nao_apaga = ["eat","tea","tan","ate","nat","bat"]
coisax_apaga = ["eat","tea","tan","ate","nat","bat"]
final = []
n=0

for n in range(0, len(coisax_apaga)):
    correto = []
    n2=0
    palavra_esc=sorted(coisax_apaga[n])
    while n2!=len(coisax_apaga):
        if palavra_esc==sorted(coisax_apaga[n2]):
            correto.append(coisax_apaga[n2])
        n2+=1
    if correto in final:
        pass
    else:
        final.append(correto)
print(final)