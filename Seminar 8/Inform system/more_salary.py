import BD

def more_salary():
    salar = int(input("Введите сумму: "))
    BD.cursor.execute("""SELECT * FROM PERSONAL WHERE salary >= ?""", (salar,))
    for one in BD.cursor.fetchall():
        print(f'ID = {one[0]}, Имя = {one[1]}, Фамилия = {one[2]}, Должность = {one[3]}, Зарплата = {one[4]}, Бонусы = {one[5]}')
    # one = BD.cursor.fetchall()
    # print(*one)

