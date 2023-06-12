from DZ3_account import card

def add_money():
    money = int(input('Введите сумму пополнения, кратную 50 у.е.'))
    if money % 50 == 0:
        card.BALANCE += money
        print(f'Вы пополнили счет на {money} у.е. ')
        card.COUNT += 1.
    else:
        print('Сумма пополнения не кратно 50 у.е.')
