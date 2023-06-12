from DZ3_account import card

def get_money() -> int:
    money = int(input('Введите сумму снятия, кратную 50 у.е.'))
    if money > card.BALANCE:
        print('Запрашиваемая сумма, больше чем сумма на счете')
    elif money % 50 == 0:
        if money * card.RATE < 30:
            rate = 30
        elif money * card.RATE > 600:
            rate = 600
        else:
            rate = money * card.RATE
        card.BALANCE = card.BALANCE - money - rate
        print(f'Вы сняли со счета {money} и проценты за снятие {rate} у.е.')
        card.COUNT += 1
    else:
        print('Сумма снятия не кратна 50 у.е.')
