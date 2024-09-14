import textwrap

# Exibe o menu e retorna a opção escolhida pelo usuário
def menu():
    """
    Função para exibir o menu de operações e capturar a opção escolhida pelo usuário.
    """
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


# Função de depósito
def depositar(saldo, valor, extrato, /):
    """
    Função que realiza o depósito em uma conta, atualizando o saldo e o extrato.
    - saldo: saldo atual da conta
    - valor: valor a ser depositado
    - extrato: histórico de transações da conta
    Retorna o saldo atualizado e o extrato.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


# Função de saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Função que realiza o saque em uma conta, respeitando as restrições de saldo, limite diário e quantidade de saques.
    - saldo: saldo atual da conta
    - valor: valor a ser sacado
    - extrato: histórico de transações da conta
    - limite: valor máximo permitido por saque
    - numero_saques: número atual de saques realizados no dia
    - limite_saques: número máximo de saques permitidos por dia
    Retorna o saldo atualizado e o extrato.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


# Função de exibição do extrato
def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta, incluindo o saldo e todas as transações realizadas.
    - saldo: saldo atual da conta
    - extrato: histórico de transações da conta
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


# Função para criar um novo usuário
def criar_usuario(usuarios):
    """
    Cria um novo usuário, armazenando as informações como CPF, nome, data de nascimento e endereço.
    - usuarios: lista de usuários existentes
    """
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")


# Função para filtrar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    """
    Filtra um usuário pelo CPF.
    - cpf: CPF do usuário
    - usuarios: lista de usuários
    Retorna o usuário encontrado ou None se não houver usuário com o CPF informado.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# Função para criar uma nova conta
def criar_conta(agencia, numero_conta, usuarios):
    """
    Cria uma nova conta bancária associada a um usuário existente.
    - agencia: número da agência bancária
    - numero_conta: número da nova conta
    - usuarios: lista de usuários cadastrados
    Retorna o dicionário da conta criada ou None se o usuário não for encontrado.
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None


# Função para listar contas existentes
def listar_contas(contas):
    """
    Exibe a lista de todas as contas bancárias cadastradas.
    - contas: lista de contas
    """
    for conta in contas:
        linha = f"""\nAgência:\t{conta['agencia']}\nC/C:\t\t{conta['numero_conta']}\nTitular:\t{conta['usuario']['nome']}\n"""
        print("=" * 100)
        print(textwrap.dedent(linha))


# Função principal para o controle do fluxo do sistema bancário
def main():
    """
    Função principal que controla o fluxo do sistema bancário, permitindo ao usuário escolher operações como
    depósito, saque, consulta de extrato, criação de contas e usuários, e listagem de contas.
    """
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
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
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Inicia o sistema bancário
if __name__ == "__main__":
    main()
