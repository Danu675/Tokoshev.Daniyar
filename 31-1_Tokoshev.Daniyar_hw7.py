import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')

conn.commit()
conn.close()

def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ("Жидкое мыло с запахом ванили", 99.99, 10),
        ("Мыло детское", 49.99, 5),
        ("Шампунь для волос", 149.99, 8),
        # Добавьте остальные товары здесь
    ]

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    conn.close()
def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    conn.close()
def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    conn.commit()
    conn.close()
def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()
def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
def get_cheap_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
def search_products(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE product_title LIKE '%' || ? || '%'", (keyword,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
add_products()
get_all_products()
update_quantity(1, 20)
update_price(2, 59.99)
delete_product(3)
get_cheap_products()
search_products("мыло")
