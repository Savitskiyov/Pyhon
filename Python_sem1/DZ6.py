numb = input("Введите число от 1 до 999: ")

if len(numb) == 1:
    a = int(numb) ** 2
    # print(f'Квадрат числа {numb} равен {int(numb) ** 2}')
elif len(numb) == 2:
    a = int(numb[0]) * int(numb[1])
    # print(f'Произведение чесел равен {int(numb[0]) * int(numb[1])}')
elif len(numb) == 3:
    a = int(str(numb)[::-1])
    # print(f'Зеркальное отображение  {int(str(numb)[::-1])}')
print(a)
