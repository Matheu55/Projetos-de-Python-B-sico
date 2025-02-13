n1 = int(input("Digite um valor: "))
n2 = int(input("Outro valor: "))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divInte = n1 // n2
poten = n1 ** n2

print("A soma é {}, \n o produto é {} e a divisão é {:.3f}".format(soma, mult, div), end=" ")
print("\nDivisão inteira {} e potência {}".format(divInte, poten))
