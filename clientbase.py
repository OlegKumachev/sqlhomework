import psycopg2


def delete_table(cur):
    cur.execute("""
        DROP TABLE contact;
        DROP TABLE client;
        """)


# Функция, создающая структуру БД (таблицы)
def create_db(cur):
    cur.execute("""CREATE TABLE client(
                id SERIAL PRIMARY KEY,
                first_name varchar(50),
                last_name varchar(50),
                email varchar(50) UNIQUE NOT NULL);
                """)
    cur.execute("""CREATE TABLE contact(
                id SERIAL PRIMARY KEY,
                client_id INT REFERENCES client(id),
                phone  INT NULL);  
                """)


# Функция, позволяющая добавить нового клиента
def add_client(cur, first_ame, last_name, email, phone=None):
    values = (first_ame, last_name, email)
    cur.execute("INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING id", values)
    client_id = cur.fetchone()[0]
    data = (client_id, phone)
    cur.execute(" INSERT INTO contact (client_id, phone) VALUES (%s,  %s)", data)


# Функция, позволяющая удалить существующего клиента
def delete_client(cur, client_id):
    cur.execute("""DELETE FROM contact WHERE client_id=%s""", (client_id,))
    cur.execute("""DELETE FROM client WHERE id =%s""", (client_id,))


# Функция, позволяющая добавить телефон для существующего клиента
def add_phone(cur, client_id, phone):
    cur.execute("""INSERT INTO contact (client_id, phone)
                    VALUES (%s, %s);""", (client_id, phone))


# Функция, позволяющая изменить данные о клиенте
def change_client(cur, client_id, first_name=None, last_name=None, email=None, phones=None):
    data = {'first_name': first_name, 'last_name': last_name, 'email': email}
    for values in data.items():
        if values[1] is not None:
            cur.execute(f"UPDATE client SET {values[0]}='{values[1]}' WHERE id='{client_id}';")
    if phones is not None:
        cur.execute("""UPDATE contact c SET phone=%s WHERE client_id=%s;""", (phones, client_id))


# Функция, позволяющая удалить телефон для существующего клиента
def delete_phone(cur, client_id, phone):
    cur.execute("""DELETE  FROM contact WHERE client_id=%s AND phone= %s""", (client_id, phone))


# Функция, позволяющая найти клиента по его данным
def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone}
    query = []
    for key, value in data.items():
        if value:
            query.append(f"{key} = '{value}'")
    criterion = 'WHERE ' + ' AND '.join(query)
    cur.execute("""
                 SELECT first_name, last_name, email, phone
                 FROM client c
                 LEFT JOIN contact co ON c.id = co.client_id
                 """ + criterion)
    res = cur.fetchone()
    return res


if __name__ == '__main__':
    with psycopg2.connect(database="clientbase", user="postgres", password="4652732-oP") as conn:
        with conn.cursor() as cur:
            create_db(cur)
            add_client(cur, 'Иван', 'Иванов', 'ivanov@email.ru')
            add_phone(cur, 1, 8915140)
            change_client(cur, 1, 'Сергей', 'Сергеев', 'sergei@email.ru', 890512345)
            find_client(cur, 'Сергей', 'Сергеев', 'sergei@email.ru', 890512345)
            delete_phone(cur, 1, 8915140)
            delete_client(cur, 1)
            delete_table(cur)
    conn.close()
