# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
import sys

BALANCE = 0
MIN = 50
MAX = 5_000_000
RATE = 0.015
BONUSRATE = 0.03
COUNT = 0
TAX = 0.1
def add_money():
    global COUNT, BALANCE
    money = int(input('Введите сумму пополнения, кратную 50 у.е.'))
    if money % 50 == 0:
        BALANCE += money
        print(f'Вы пополнили счет на {money} у.е. ')
        COUNT += 1.
    else:
        print('Сумма пополнения не кратно 50 у.е.')

def add_bonus():
    global BONUSRATE, BALANCE
    BONUSSUM = BALANCE * BONUSRATE
    BALANCE += BALANCE * BONUSRATE
    print(f'начислен бонус {BONUSSUM}')

def get_money() -> int:
    global COUNT, BALANCE, RATE
    money = int(input('Введите сумму снятия, кратную 50 у.е.'))
    if money > BALANCE:
        print('Запрашиваемая сумма, больше чем сумма на счете')
    elif money % 50 == 0:
        if money * RATE < 30:
            rate = 30
        elif money * RATE > 600:
            rate = 600
        else:
            rate = money * RATE
        BALANCE = BALANCE - money - rate
        print(f'Вы сняли со счета {money} и проценты за снятие {rate} у.е.')
        COUNT += 1
    else:
        print('Сумма снятия не кратна 50 у.е.')


while True:
    print(f'Cумма на счету составляет {BALANCE} у.е.')
    print('Выберите действие:\n\
1 - пополнить\n\
2 - снять\n\
3 - выйти')
    choise = input("Введите цифру: ")
    if BALANCE > MAX:
        TAXE = BALANCE * TAX
        BALANCE -= TAXE
        print(f'С вас списали налог на богатство в размере {TAXE}')

    match choise:
        case '1':
            add_money()
            #print(f'Cумма на счету составляет {card.BALANCE} у.е.')
        case '2':
            get_money()
            #print(f'Cумма на счету составляет {card.BALANCE} у.е.')
        case '3':
            sys.exit()

    if COUNT % 3 == 0:
        add_bonus()
    else:
        pass
