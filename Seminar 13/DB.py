import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Ibd23hjy",
        db='vk',
    )

    cur = conn.cursor()

    # Select query
    cur.execute("select * from sakila.film")
    output = cur.fetchall()

    for i in output:
        print(i)

    # To close the connection
    conn.close()


# Driver Code
#if __name__ == "__main__":
#    mysqlconnect()

mysqlconnect()
