#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
#на указанных позициях. Позиции хранятся в списке positions - создайте этот список
# (например:positions = [1, 3, 6]).

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
