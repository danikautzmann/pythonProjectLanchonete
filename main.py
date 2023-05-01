print('Bem vindo a lanchonete da Daniela!!')
print('********** Cardápio **********')
print('|Código| | Descrição            | | Valor     |')
print('|100   | | Cachorro-quente      | | R$ 9,00   |')
print('|101   | | Cachorro-quente duplo| | R$ 11,00) |')
print('|102   | | X-Egg                | | R$ 12,00  |')
print('|103   | | X-Salada             | | R$ 13,00  |')
print('|104   | | X-Bacon              | | R$ 14,00  |')
print('|105   | | X-Tudo               | | R$ 17,00  |')
print('|200   | | Refrigerante Lata    | | R$5,00    |')
print('|201   | | Chá Gelado           | | R$4,00    |')
valortotal = 0
opcao = 1

while (opcao == 1):
    codigo = int(input('\nDigite o código do produto desejado:'))
    if codigo == 100:
        valortotal += 9
        print('Você pediu um cachorro-quente no valor de R$ 9,00.')
    elif codigo == 101:
        valortotal += 11
        print('Você pediu um Cachorro-quente duplo no valor de R$ 11,00.')
    elif codigo == 102:
        valortotal +=12
        print('Você pediu um X-Egg no valor de R$12,00.')
    elif codigo == 103:
        valortotal += 13
        print('Você pediu um Xis-Salada no valor de R$13,00.')
    elif codigo == 104:
        valortotal += 14
        print('Você pediu um Xis-Bacon no valor de R$14,00.')
    elif codigo == 105:
        valortotal += 17
        print('Você pediu um Xis-Tudo no valor de R$17,00.')
    elif codigo == 200:
        valortotal+=5
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
    elif codigo == 201:
        valortotal += 4
        print('Você pediu um Chá Gelado no valor de R$4,00.')
    else:
        print('Este código de produto não existe, digite uma opção válida.')

    opcao = int(input('Deseja fazer um novo pedido?\n1 - SIM\n0 - NÃO\n'))
    continue

print('O total a ser pago é:R$ {:.2f}'.format(valortotal))







