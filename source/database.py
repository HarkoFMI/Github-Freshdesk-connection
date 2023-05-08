import sqlite3

connection = sqlite3.connect('database')
cursor = connection.cursor()


def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login_name TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    creation_date TEXT NOT NULL)''')


def insert_user(login, name, creation_date):
    cursor.execute('''SELECT * FROM users
                          WHERE login_name = ? AND full_name = ? AND creation_date = ?''',
                   (login, name, creation_date))
    existing_record = cursor.fetchone()

    if existing_record:
        print("This user already exists in the database")
    else:
        cursor.execute('''INSERT INTO users (id, login_name, full_name, creation_date)
                              VALUES (NULL, ?, ?, ?)''', (login, name, creation_date))
    connection.commit()


def close_db():
    cursor.close()
    connection.close()

