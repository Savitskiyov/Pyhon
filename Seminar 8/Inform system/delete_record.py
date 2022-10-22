import BD

def del_record():
    ID_number = int(input("Введите ID, которое будем удалять: "))
    BD.cursor.execute(f'DELETE FROM PERSONAL WHERE ID = {ID_number}')
    BD.bd.commit()
    print(f'Запись c {ID_number} удалена')

