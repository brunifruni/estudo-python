menu = """\n
    ================ MENU ================
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [q]Sair

    => """

saldo = 0
limite = 500
extrato= ""
num_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "d":
        valor =  float(input("Informe o valor do depósito: "))

        if valor > 0:#para evitar deposito de num negativo
            saldo += valor #saldo + valor = saldo
            extrato += f'Depósito: R${valor:.2f}\n'

        else:
            print ("Operação falhou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor + saldo

        excedeu_limite = valor + limite

        excedeu_saques = num_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Saldo Insuficiente.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor #saldo - valor = saldo
            extrato += f'Saque: R$ {valor:.2f}\n'
            num_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'e':
        print('\n==========EXTRATO==========')
        print('Não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\n Saldo: R${saldo:.2f}')
        print('=============================')

    elif opcao =='q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")

