# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = 'ывлдодло цлазоцзщкпо овылаоыабвцлоа ывзлаоц авбцоуа'

def sort_t(ar):
    for i in ar:
        if "абв" in i:
            ar.remove(i)
    list_array = " ".join(ar)
    return list_array

srt = txt.split()
print(srt)
print(f'Результат 1: {(sort_t(srt))}')


# 2 вариант

lst = [i for i in txt.split() if "абв" not in i]
print(f'Результат 2: {" ".join(lst)}')