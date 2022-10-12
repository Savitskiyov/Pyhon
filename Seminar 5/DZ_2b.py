# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 1) # флаг очередности


# Функция по которой проверяется кол-во взятых конфет
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

# рандомный выбор первого игрока
if flag == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

# Интеллект бота
def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# Подсчет кол-ва взявших конфет
counter1 = 0
counter2 = 0

while value > 28:
    if flag == 1:
        k = input_dat(player1)
        counter1 += k # Кол-во взявших у игрока
        value -= k # Кол-во оставшихся у игрока
        flag = False # смена хода
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,28) # Берет рандомное число
        counter2 += k # Кол-во взявших у бота
        value -= k # Кол-во оставшихся у бота
        flag = True # смена хода
        p_print(player2, k, counter2, value)

if flag == 1:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")