import psycopg2
from configparser import ConfigParser

# Функция для чтения конфигурации из файла settings.ini
def config(filename='settings.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return db

# Функция для создания таблиц из SQL-скрипта
def create_tables():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open('create_tables.sql', 'r') as f:
            cur.execute(f.read())
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Функция для вставки клиента в таблицу clients
def insert_client(first_name, last_name, email):
    sql = """INSERT INTO clients(first_name, last_name, email, registration_date)
             VALUES(%s, %s, %s, CURRENT_DATE) RETURNING client_id;"""
    conn = None
    client_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name, last_name, email))
        client_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return client_id

# Функция для выполнения параметрического запроса
def get_clients_by_email(email):
    sql = "SELECT * FROM clients WHERE email = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (email,))
        rows = cur.fetchall()
        print(f"Clients with email {email}:")
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Основной блок для выполнения функций
if __name__ == '__main__':
    create_tables()
    insert_client('Andrey', 'Suchov', 'Andrey.Suchov@mail.com')
    insert_client('Andrey', 'Kozlov', 'andrey.kozlov@gmail.com')
    insert_client('dfnasjkfna', 'sdASDJJDIJ', 'BHsbci.doidiaj@gmail.com')

    # Параметрический запрос с переменной
    param = 'Andrey.Suchov@mail.com'
    get_clients_by_email(param)
    print('')

    param = 'BHsbci.doidiaj@gmail.com'
    get_clients_by_email(param)
    print('')
    
    param = 'andrey.kozlov@gmail.com'
    get_clients_by_email(param)
    
