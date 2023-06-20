# ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение лучше многострочное

MIN = 0
MAX = 101

def gen_num(min, max):
    for i in range(min, max):
        if i % 15 == 0:
            yield 'FizzBuzz'
        elif i % 3 == 0:
            yield 'Fizz'
        elif i % 5 == 0:
            yield 'Buzz'
        else:
            yield i

a = gen_num(MIN,MAX)
print(*a, sep='\n')


generatore = ('FizzBuzz' if i % 15 == 0 else \
              'Fizz' if i % 3 == 0 else \
              'Buzz' if i % 5 == 0else i for i in range(MIN, MAX))


print(*generatore, sep='\n')