# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in [[2, 3, 4, 5], [6, 7, 8, 9]]:
    if i != 0:
        print("")
    for k in range(2, 10):
        print('%s * %s = %s\t\t\t' % (i[0], k, i[0] * k),
              '%s * %s = %s\t\t\t' % (i[1], k, i[1] * k),
              '%s * %s = %s\t\t\t' % (i[2], k, i[2] * k),
              '%s * %s = %s\t\t\t' % (i[3], k, i[3] * k))





