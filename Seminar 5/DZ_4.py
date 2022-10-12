# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https://ru.wikipedia.org/wiki/Кодирование_длин_серий

lst ='WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def comp_rule(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]: # перебор повторяющихся значений
            count += 1 # подсчет повторяющихся значений
        else:
            res = res + str(count) + txt[i] # Запись подсчета
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]): # Запись для последних символов
        res = res + str(count) + txt[-1]
    return res

def decomp_rule(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha(): #возвращает True, если все символы в строке str являются буквенными
            number += txt[i]
        else:
            res = res + txt[i] * int(number) #перемножение на кол-во цифр
            number = ''
    return res


# s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {comp_rule(lst)}")
print(f"Текст после дешифровки: {decomp_rule(comp_rule(lst))}")