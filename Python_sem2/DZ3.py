# Задание на семинаре
#  Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

from DZ3_add_money import add_money
from DZ3_get_money import get_money
from DZ3_account import card
from DZ3_bonus import add_bonus


while True:
    print('Выберите действие:\n\
1 - пополнить\n\
2 - снять\n\
3 - выйти')
    choise = input("Введите цифру: ")
    ("Введите цифру: ")
    if card.BALANCE > card.MAX:
        TAX = card.BALANCE * card.TAX
        card.BALANCE -= TAX
        print(f'С вас списали налог на богатство в размере {TAX}')

    match choise:
        case '1':
            add_money()
            print(f'Cумма на счету составляет {card.BALANCE} у.е.')
        case '2':
            get_money()
            print(f'Cумма на счету составляет {card.BALANCE} у.е.')
        case '3':
            quit()

    if card.COUNT % 3 == 0:
        print(add_bonus())
    else:
        pass