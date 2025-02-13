import random

n1 = str(input("Primeiro nome: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceito nome: "))
n4 = str(input("Quato nome: "))
n5 = str(input("Quinto nome: "))

lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))