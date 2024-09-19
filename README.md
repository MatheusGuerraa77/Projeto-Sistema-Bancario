# Projeto-Sistema-Bancario
 Neste projeto, tive a oportunidade de desenvolver um Sistema Bancário em Python junto com conteúdo do bootcamp da NTT DATA, criei um sistema funcional que realiza transações bancárias, proporcionando uma experiência prática no desenvolvimento de software.

Este projeto implementa um sistema bancário, com funcionalidades típicas de gerenciamento de clientes, contas e transações financeiras, como saques, depósitos e consultas de extrato. A aplicação utiliza orientação a objetos para estruturar as entidades envolvidas (clientes, contas, transações, histórico, etc.) e permite interação através de um menu simples no terminal.

# Estrutura do Projeto:
Classes Principais:

Cliente: Representa um cliente do banco, com um endereço e a capacidade de realizar transações em suas contas. A subclasse PessoaFisica estende Cliente, adicionando atributos como nome, data de nascimento e CPF.
Conta: Representa uma conta bancária, com saldo, número da conta, agência, cliente associado e histórico de transações. A subclasse ContaCorrente estende Conta, incluindo limites de saque e quantidade de saques diários permitidos.
Transacao (abstract): Uma classe abstrata que define a estrutura para transações. Duas subclasses, Saque e Deposito, implementam transações específicas e registram suas ocorrências no histórico.
Historico: Registra as transações de uma conta, armazenando informações como tipo de transação, valor e data.
# Funcionalidades:

- Criar Cliente: O usuário pode criar um novo cliente fornecendo o CPF, nome, data de nascimento e endereço.
- Criar Conta: O usuário pode criar uma nova conta corrente para um cliente existente.
- Depositar e Sacar: São implementadas as funções de depósito e saque em uma conta, incluindo validações de saldo, limite e quantidade de saques permitidos.
- Exibir Extrato: Exibe todas as transações realizadas em uma conta e o saldo atual.
- Listar Contas: Exibe todas as contas criadas no sistema, com detalhes como agência, número da conta e titular.
# Lógica do Menu:

O projeto possui um loop principal que exibe um menu com opções para depositar, sacar, criar contas e clientes, listar contas e sair do sistema.
# Funcionalidades adicionais e limitações:
- Limites de saque: Cada conta corrente tem um limite de saque diário e de número de saques que pode ser realizado.
- Histórico de transações: Cada conta mantém um histórico das transações, que podem ser consultadas a qualquer momento.
- Limitação de conta única: Atualmente, o sistema permite que um cliente tenha apenas uma conta (não há lógica para seleção de contas se o cliente tiver várias).