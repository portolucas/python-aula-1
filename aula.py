# -*- coding: utf-8 -*-
import random as rd

# Isto é um comentário

print("Olá mundo")

""" 
Esse já é um 
comentário
de muitas linhas
"""

print("Tchau mundo")

list = ["Maçã", "Banana", "Laranja"]

for fruta in list:
    print(fruta)


for i in range(10, 20, 3):
    print(i)

string = "Olá"

for i in string:
    print(i)

numero = rd.randint(1, 10)
print(numero)

pessoa = rd.choice(["A", "B", "C"])
print(pessoa)

a = 50
b = 0

try:
    c = a/b
except:
    print("Não é possível dividir por zero")

dic = {"chave": "valor", "outrachave": "outrovalor"}
print(dic['chave'])
for i in dic:
    print(dic[i])
for item in dic.items():
    print(item)
for valor in dic.values():
    print(valor)
for chave in dic.keys():
    print(chave)


class Cachorro:
    tipo = "canino"

    def __init__(self, name):
        self.name = name

cao = Cachorro('Nina')
print(cao.name)

## Python Set

## Set é uma coleção não ordenada e não indexada.

thisset = {"Apple", "Banana", "Cherry"}
print(thisset)

## Uma tupla é uma coleção ordenada e imutável
thistuple = ("Apple", "Banana", "Cherry")
print(thistuple)


