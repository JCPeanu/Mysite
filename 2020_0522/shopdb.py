import sqlite3
#conn = sqlite3.connect('myshop.db')

def create_table(conn):
    c = conn.cursor()
    sql = """
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        desc TEXT NOT NULL,
        image TEXT NOT NULL
    )
    """
    c.execute(sql)

    conn.commit()
    conn.close()

def insert_product(conn, name, price, desc, img):
    c = conn.cursor()
    sql = """
    INSERT INTO products (name, price, desc, image)
    VALUES (?, ?, ?, ?)
    """
    c.execute(sql, (name, price, desc, img))
    conn.comit()