# Adivenhe o número :)))
import random
import os


def regras():
    print("1 - O sistema irá gerar um numero aleatorio")
    print("2 - O numero será de 1 a 10")
    print("3 - Você deve tentar adivinhar qual o número")
    print("4 - Se acertar ganhará um ponto")
    print("Use o comando limpa para apagar tudo")


def limpa():
    os.system('cls')  # usado para limpar a tela


def play(escolha):  # def usado para criar a função
    aleatorio = random.randint(a=1, b=10)
    acerto = 0
    traco = "----------------------------------------------"
    regras()
    limpa()
    if aleatorio == escolha:
        print("Você acertou, parabéns!!")
        acerto = acerto + 1  # adicionar valor +1 p/ variável
        print(traco)
        print("Sua pontuação é de " + str(acerto))
    else:
        print("Infelizmente você errou :( mas não desista :)")
        acerto = acerto + 0
        print(traco)  # organização do codigo na hora de imprimi
        print("Sua pontuação é de " + str(acerto))
        print(traco)
        print("O número correto era: " + str(aleatorio))


if __name__ == '__main__':
    regras()
    escolha = int(input("Qual o número gerado?"))
    play(escolha)
    limpa()
