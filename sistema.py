menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao =='d':
        valor = float(input('informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            
        else:
            print('operação falhou: o valor informado é inválido.')
            
    elif opcao == 's':
        valor = float(input(f'Informe o valor do saque: '))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_sasques = valor > numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou: Você não tem saldo suficiente.')
            
        elif excedeu_limite:
            print('Operação falhou: O valor do saque excede o limite.')
        
        elif excedeu_sasques:
            print('Operação falhou: número máximo de saques excedido.')
            
        elif valor > 0:
            
            