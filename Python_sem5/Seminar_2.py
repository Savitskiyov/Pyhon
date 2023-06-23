# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы из Unicode.
# ✔ Напишите преобразование в одну строку.
text = set(input('Введите текст: '))
my_func = {val: ord(val) for val in text}
print(my_func)

