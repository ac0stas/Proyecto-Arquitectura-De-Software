import sqlite3

conn = sqlite3.connect('inventario.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE Product (
        SKU INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        Stock INTEGER NOT NULL
    )
''')
conn.commit()
conn.close()
