# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

numb = int(input("Введите количество рядов: "))
spaces = numb-1
stars = 1
for i in range(numb):
    print(
              (' '*spaces) +
              ('*'*stars) +
              (' '*spaces)
          )
    stars += 2
    spaces -= 1
