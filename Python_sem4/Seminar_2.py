# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

text = 'llhelllppp!^'
def my_func (val):
    my_text = set(val)
    spisok_res = []
    for item in my_text:
        spisok_res.append(ord(item))
    return sorted(spisok_res)


print(*my_func(text))