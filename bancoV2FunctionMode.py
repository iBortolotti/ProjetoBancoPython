from datetime import date, datetime, time
import os
import time
import textwrap
os.system('clear')

data_atual = date.today()
data_formatada = f"{data_atual.day:02d}/{data_atual.month:02d}/{data_atual.year}"

def format_cpf(cpf_sem_formatacao):
  # Validação básica do CPF (tamanho e formato)
  if cpf_sem_formatacao == "":
    Error_msg("CPF não foi informado operação cancelada !!!.")
    return
  # Verifica se cpf foi digitado
  elif not len(cpf_sem_formatacao) == 11 or not cpf_sem_formatacao.isdigit():
    Error_msg("O CPF Digitado não está correto !!!.")
    return
  # Formatação do CPF
  cpf_formatado = f"{cpf_sem_formatacao[:3]}.{cpf_sem_formatacao[3:6]}.{cpf_sem_formatacao[6:9]}-{cpf_sem_formatacao[9:]}"
  return cpf_formatado

def menu():
    # os.system('clear')
    menu = """\033[A
    \033[48;5;202m\033[10D================ MENU ================\033[0;0m
    \033[10D[d]  Depositar
    \033[10D[s]  Sacar
    \033[10D[e]  Extrato
    \033[10D[nc] Nova conta
    \033[10D[lc] Listar contas
    \033[10D[nu] Novo usuário
    \033[10D[q]  Sair
    \033[10D=>\033[0;0m """
    return input(textwrap.dedent(menu))

def menu_logo(msg):
    os.system('clear')
    menuMsg = f"""\033[48;5;202m================ {msg} ================\033[0;0m
    """
    print(menuMsg)
    # time.sleep(3)
    return

def Error_msg(msg,temp=3):
    print(f"\033[1A\033[K\033[31;43m{msg}\033[0;0;202m")
    time.sleep(temp)
    os.system('clear')

def Valid_msg(msg,tmp=3):
    print(f"\033[1A\033[K\033[32m{msg}\033[0m")
    time.sleep(tmp)
    os.system('clear')

def depositar(saldo, valor, extrato, /):
    # if valor > 0 and not valor.isdigit():
    if valor > 0:
        saldo += valor
        extrato += f"\033[34m{data_formatada}\033[0m \033[32mDepósito: R$ {valor:.2f}\033[0m\n"
        Valid_msg("Valor Depositado com sucesso !!!")
    else:
        Error_msg("Operação falhou! O valor informado é inválido !!!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
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
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
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

def criar_usuario(usuarios):
    menu_logo("Cadastro de Novo Usuario")

    cpf = format_cpf(input("Informe o CPF (somente número): "))
    usuario = filtrar_usuario(cpf, usuarios)
    if not cpf:
        return 
    elif usuario:
        Error_msg("Já existe usuário com esse CPF!.")
        return
    else:
        # nome = input("Informe o nome completo: ")
        while (nome := input("Informe o nome completo: ")) == "":
            Error_msg("campo de nome é obrigatorio !!!.")
        
    #  while True:
    #     nome = input("\033[A\033[0KInforme o nome completo: ")
    #     if not(nome.strip()):  # Verifica se o nome não está vazio
    #         print("\033[1A\033[K\033[31;43mO campo de nome é obrigatório!!!\033[0;0;202m")
    #         time.sleep(3) 
    #         break  # Sai do loop se o nome foi preenchido

          
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    userCreated = usuarios[-1]
    os.system('clear')
    Valid_msg("Usuário criado com sucesso !!!.",1)
    print(f"""Olá {userCreated["nome"]}, Seja bem vindo !!!!
    CPF cadastrado: {userCreated["cpf"]}
    Data de Nascimento: {userCreated["data_nascimento"]}
    Endereço: {userCreated["endereco"]}
    """)
    time.sleep(3)
    os.system('clear')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = format_cpf(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        Valid_msg("Conta criada com sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    Error_msg("Usuário não encontrado, fluxo de criação de conta encerrado!!!")

def listar_contas(contas):
    menu_logo("Contas cadastradas!!")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 54)
        print(textwrap.dedent(linha))
    input("Digite uma tecla para sair!!")
    os.system('clear')

def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            os.system('clear')
            break

        else:
            Error_msg("\nOperação inválida, por favor selecione novamente a operação desejada !!!!.")
            os.system('clear')

main()
