import psycopg2

def delete_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE contact;
        DROP TABLE client;
        """)


# Функция, создающая структуру БД (таблицы)
def create_db(conn):
    with conn.cursor() as cur:
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
def add_client(conn, f_name, l_name,  email, phone=None):
    values = (f_name, l_name, email)
    with conn.cursor() as cur:
        cur.execute("INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s) RETURNING id", values)
        client_id = cur.fetchone()[0]
        date = (client_id, phone)
        cur.execute(" INSERT INTO contact (client_id, phone) VALUES (%s,  %s)", date)


# Функция, позволяющая удалить существующего клиента
def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM contact WHERE client_id=%s""", (client_id,))
        cur.execute("""DELETE FROM client WHERE id =%s""", (client_id,))


# Функция, позволяющая добавить телефон для существующего клиента
def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO contact (client_id, phone)
                        VALUES (%s, %s);""", (client_id, phone))


# Функция, позволяющая изменить данные о клиенте
def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        cur.execute("""UPDATE client c SET first_name=%s, last_name=%s, email=%s
                        WHERE id=%s
                        """, (first_name, last_name, email,  client_id))
        cur.execute("""UPDATE contact c SET phone=%s WHERE client_id=%s;""", (phones, client_id))


# Функция, позволяющая удалить телефон для существующего клиента
def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""DELETE  FROM contact WHERE client_id=%s AND phone= %s""", (client_id, phone))


# Функция, позволяющая найти клиента по его данным
def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""SELECT c.first_name, c.last_name, c.email, c2.phone  FROM client c
                        LEFT JOIN contact c2 ON c.id = c2.client_id
                        WHERE first_name=%s OR last_name=%s OR email=%s OR phone=%s; 
                        """, (first_name, last_name, email, phone))

        return cur.fetchone()


with psycopg2.connect(database="clientbase", user="postgres", password="postgres") as conn:
    create_db(conn)
    add_client(conn, "Илья", "Моровлин", "udelnay@rus.ru", 120033)
    add_phone(conn, 1, 331200)
    delete_phone(conn, 1, 331200)
    change_client(conn, 1, 'Алексей', "Добров", "pravda@.com", 4859328)
    find_client(conn, 'Алексей', "Добров", "pravda@.com" )
    delete_client(conn, 1)


conn.close()