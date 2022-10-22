import BD

def find_record():
    id_num = int(input("Введите ID: "))
    BD.cursor.execute(f'SELECT * FROM PERSONAL WHERE id like {id_num};')
    for one in BD.cursor.fetchall():
        print(f'ID = {one[0]}, Имя = {one[1]}, Фамилия = {one[2]}, Должность = {one[3]}, Зарплата = {one[4]}, Бонусы = {one[5]}')
