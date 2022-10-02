#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
#на указанных позициях. Позиции хранятся в списке positions - создайте этот список
# (например:positions = [1, 3, 6]).

# 1 вариант
n = int(input("Введите число n:"))
positions = [1, 3, 6]
x = max(positions)
y = int(len(positions))
my_str = []

for i in range(-n, n+1):
    my_str.append(i)

total = int(1)
if len(my_str) < x:
    print(f'Необходимо ввести значение больше ')
else:
    for i in range(1, y+1):
        total *= my_str[positions[i-1]]
print(total)


# 2 вариант

def new_spisok(n, n1, n2, n3):
    res = []
    poz = [n1,n2,n3]
    result = 1
    for i in range(-n, n+1):
        res.append(i)
    maxindex = len(res)-1
    minindex = len(res)
    for n in poz:
        if n > maxindex or n < -minindex:
            return print("Неверное указали значения индекса")
        result *= res[n]
    return print (f'В списке {res}, произведение значений с индексами  {n1},{n2},{n3} составляет {result}')

number = int(input("Введите число n:"))
poz1 = int(input("Введите индекс первого числа:"))
poz2 = int(input("Введите индекс первого числа:"))
poz3 = int(input("Введите индекс первого числа:"))

new_spisok(number, poz1, poz2, poz3)