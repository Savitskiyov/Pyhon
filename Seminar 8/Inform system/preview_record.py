import BD

def preview_record():
    # BD.cursor.execute("select * from personal;")
    # two = BD.cursor.fetchall()
    # print(*two)
    for i in BD.cursor.execute("select * from personal;"):
        print(f'ID = {i[0]}, Имя = {i[1]}, Фамилия = {i[2]}, Должность = {i[3]}, Зарплата = {i[4]}, Бонусы = {i[5]}')
