# Jogo de perguntas simples
pontuacao = 0

print("Bem-vindo ao Jogo das Perguntas!")

#Pergunta 1
resposta = input("Qual a capital da França? ")
if resposta.lower() == "paris":
    print("Correto!")
    pontuacao +=1
else:
    print("Errado!")

#Pergunta 2
resposta = input("Qual o maior planeta do sistema solar? ")
if resposta.lower() == "júpiter" or resposta.lower() == "jupiter":
    print("Correto!")
    pontuacao +=1
else:
    print("Errado!")

#Perfunta 3
resposta = input("Quanto é 5 + 5? ")
if resposta == "10":
    print("Correto!")
    pontuacao +=1
else:
    print("Errado!")

#Exiba a pontação final
print(f"Sua pontuação final é: {pontuacao} de 3")
