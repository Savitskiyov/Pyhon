import BD

def update_record ():
    id_num = int(input("Введите ID у кого меняем: "))
    salar = int(input("Введите новую зарплату: "))
    upd = (f'UPDATE personal set salary = {salar} where id = {id_num}')
    BD.cursor.execute(upd)
    BD.bd.commit()
    print("Зарплату поменяли")
