import BD

def add_record():
    ID_number = int(input("Введите ID: "))
    last_nm = input("Введите фамилию: ")
    first_nm = input("Введите имя: ")
    posit = input("Введите Должность: ")
    sal = int(input("Введите сумму зарплаты: "))
    bon = int(input("Введите сумму бонуса: "))
    BD.cursor.execute("""INSERT INTO personal(id, name, last_name, position, salary, bonus) VALUES (?, ?, ?, ?, ?, ?)""", (ID_number, last_nm, first_nm, posit, sal, bon))
    BD.bd.commit()
    print("Запись успешно вставлена")

