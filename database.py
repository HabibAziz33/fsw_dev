import sqlite3

database = sqlite3.connect('fsw.db')
cursor = database.cursor()


def user():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            phone TEXT
        )
        ''')


def product():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            product_description TEXT
    ) 
    ''')
