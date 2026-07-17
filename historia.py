from par_ou_impar import par

while True:
    print ("Olá, tudo bem coleguinha?")
    print ("\nO nosso programa contém as seguintes funcões: \n1 - Calculadora (Murilo)\n2 - Descubra se é par ou impar (Adalberto)\n3 - Sair")
    escolha = input("\nDigite qual função você deseja ver primeiro!: ")
    if escolha == "1":
        print ("Coloque o seu código a partir daqui")
    if escolha == "2":
        print("\nBem vindo a função de identificação dos números!")
        num = int (input("\nInsira um número: "))
        if par(num):
            print ("\nÉ par\n")
        else:
            print ("\nÉ impar\n")
    if escolha == "3":
        print("\nSaindo do programa...")
        break
    