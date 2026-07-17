
from par_ou_impar import par
from funcao_calculadora import calculadora

while True:
    print ("Olá, tudo bem coleguinha?")
    print ("\nO nosso programa contém as seguintes funcões: \n1 - Calculadora (Murilo)\n2 - Descubra se é par ou impar (Adalberto)\n3 - Sair")
    escolha = input("\nDigite qual função você deseja ver primeiro!: ")
    if escolha == "1":
        print("Você escolheu a função do Murilo!!!\n\n")

        a=int(input("Digite o primeiro número: "))
        b=int(input("Digite o segundo número: "))

        print("\nEscolha a operação: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        operacao=int(input("Digite o número da operação: "))

        resultado=calculadora(a, b, operacao)
        print("O resultado é: %.2f \n\n" %resultado)
        
    if escolha == "2":
        print("\nVocê escolheu a função do Adalberto!!! ")
        num = int (input("\nInsira um número: "))
        if par(num):
            print ("\nÉ par\n")
        else:
            print ("\nÉ impar\n")
    if escolha == "3":
        print("\nSaindo do programa...")
        break