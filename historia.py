from funcao_calculadora import calculadora
from par_ou_impar import par


while True:

    print("Olá, tudo bem amiguinhos!!!")
    print("1 - Função do Murilo (Calculadora)")
    print("2 - Função do Adalberto (Par ou Ímpar)")
    print("0 - Sair do programa")

    opcao=int(input("Digite a opção: "))

    if opcao==1:
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

    elif opcao==2:
        par()

    elif opcao==0:
        print("Saindo do programa...")
        break

    else:
        print("Opção Inválida, escolha somente a opção 1, 2 ou 0\n")