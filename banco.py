from datetime import date, datetime, time
import os
import time
os.system('clear')

menu = """\033[H
    \033[48;5;202m================ MENU ================\033[0;0m
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    =>\033[0;0m"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

data_atual = date.today()
data_formatada = f"{data_atual.day:02d}/{data_atual.month:02d}/{data_atual.year}"

print("\033[H") #Cursor Home (0,0)
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            print("\033[1A\033[K\033[32mValor Depositado com sucesso !!!\033[0m")
            time.sleep(2)
            saldo += valor
            extrato += f"\033[34m{data_formatada}\033[0m \033[32mDepósito: R$ {valor:.2f}\033[0m\n"
            os.system('clear')
        else:
            print("\033[1A\033[K\033[31;43mOperação falhou! O valor informado é inválido.\033[0;0;202m")
            time.sleep(3)
            os.system('clear')
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("\033[1A\033[K\033[31;43mOperação falhou! Você não tem saldo suficiente.\033[0;0;202m")
            time.sleep(3)
            os.system('clear')
        elif excedeu_limite:
            print("\033[1A\033[K\033[31;43mOperação falhou! O valor do saque excede o limite.\033[0;0;202m")
            time.sleep(3)
            os.system('clear')
        elif excedeu_saques:
            print("\033[1A\033[K\033[31;43mOperação falhou! Número máximo de saques excedido.\033[0;0;202m")
            time.sleep(3)
            os.system('clear')
        elif valor > 0:
            saldo -= valor
            extrato += f"\033[34m{data_formatada}\033[0m \033[31mSaque:    R$ -{valor:.2f}\033[0m\n"
            numero_saques += 1
            print("\033[1A\033[K\033[32mSaque realizado com sucesso !!!\033[0m")
            time.sleep(2)
            os.system('clear')
        else:
            print("\033[1A\033[K\033[31;43mOperação falhou! O valor informado é inválido.\033[0;0;202m")
            time.sleep(3)
            os.system('clear')
    elif opcao == "e":
        os.system('clear')
        print(f"\n================ EXTRATO =================") 
        print("Não foram realizadas movimentações." if not extrato else extrato)
        if saldo > 0:
            print(f"\n\033[32mSaldo: R$ {saldo:.2f}\033[0m")
        else:
            print(f"\n\033[33mSaldo: R$ {saldo:.2f}\033[0m")
        print("==========================================")
        input("Precione Qualquer tecla para sair!!!!")
        os.system('clear')

    elif opcao == "q":
        os.system('clear')
        break

    else:
        print("\033[31;43mOperação inválida, por favor selecione novamente a operação desejada.\033[0;0;202m")
        time.sleep(3)
        os.system('clear')