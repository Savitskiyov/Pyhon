# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


N = 8
x = []
y = []


def inp():
    for i in range(N):
        new_x, new_y = [int(s) for s in input(f'введите {i + 1} пару чисел на доске 8×8, через пробел:').split()]
        x.append(new_x)
        y.append(new_y)


def check(x1, y1):
    correct = True
    for i in range(N):
        for j in range(i + 1, N):
            if x1[i] == x1[j] or y1[i] == y1[j] or abs(x1[i] - x1[j]) == abs(y1[i] - y1[j]):
                correct = False

    if correct is True:
        return False
    else:
        return True

if __name__ == '__main__':
    inp()
    print(x)
    print(y)
    # print(check(x, y))

