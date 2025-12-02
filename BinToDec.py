def Opção_1_PT():
    Decimal = int(input("Digite o número decimal: "))
    Binário = bin(Decimal).replace("0b", "")
    print("O seu número em binário é: ", Binário)

def Opção_2_PT():
    Binário2 = input("Digite o número binário: ")
    Decimal2 = int(Binário2, 2)
    print(f"O seu número em decimal é: {Decimal2}")

def Option_1_EN():
    Decimal = int(input("Type your decimal number here: "))
    Binário = bin(Decimal).replace("0b", "")
    print("Your binary number is: ", Binário)

def Option_2_EN():
    Binário2 = input("Type your binary number here: ")
    Decimal2 = int(Binário2, 2)
    print(f"Your decimal number is: {Decimal2}")

print("Welcome! - Bem-Vindo!")
print("")
print("1 - Português/Portuguese")
print("2 - Inglês/English")
print("")
Lingua = input("Escolha uma língua /nChoose an language: ")

if Lingua == "1":
    while True:
        print("-------------------------------------")
        print("BEM VINDO AO CONVERSOR DE VALORES")
        print("")
        print("Escolha uma opção:")
        print("")
        print("Digite o número 1 para converter Decimal para Binário")
        print("Digite o número 2 para converter Binário para Decimal")
        print("Digite o número 3 para encerrar o programa")
        print("")

        Escolha = int(input("Digite sua escolha: "))

        if Escolha == 1:
            Opção_1_PT()
        elif Escolha == 2:
            Opção_2_PT()
        elif Escolha == 3:
            print("Programa encerrado")
            break
        else:
            print("")
            print("ERRO: Você escolheu o número inválido para esta operação")
else:
    while True:
        print("-------------------------------------")
        print("WELCOME TO THE BINARY/DECIMAL VALUE CONVERTER")
        print("")
        print("Choose an option:")
        print("")
        print("Press number 1 for convert decimal to binary")
        print("Press number 2 for convert binary to decimal")
        print("")

        Escolha = int(input("Type your option: "))

        if Escolha == 1:
            Option_1_EN()
        elif Escolha == 2:
            Option_2_EN()
        elif Escolha == 3:
            print("The program stopped")
            break
        else:
            print("")
            print("ERROR: You chose a wrong number for this operation")