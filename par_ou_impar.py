def par(n):
    if (n%2) ==0:
        return True
    else:
        return False
while True:
    num = int (input("\nInsira um número: "))
    if par(num):
         print ("\nÉ par")
    else:
         print ("\nÉ impar")
    break