def par(n):
    if (n%2) ==0:
        return True
    else:
        return False

def rodar():
    while True:
        num = int (input("\nInsira um número: "))
        if par(num):
            print ("\nÉ par")
        else:
            print ("\nÉ impar")
        
if __name__ == "__main__":
    rodar()
