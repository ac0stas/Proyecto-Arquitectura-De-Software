import sqlite3

def create_product(name, price, sku, stock):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute("INSERT INTO Product VALUES (?, ?, ?, ?)", (sku, name, price, stock))
    conn.commit()
    conn.close()
