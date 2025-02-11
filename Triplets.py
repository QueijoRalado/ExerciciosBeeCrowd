import random

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

'''

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