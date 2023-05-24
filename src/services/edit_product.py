import sqlite3

def edit_product(name, price, sku, stock):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute("UPDATE Productos SET Nombre=?, Precio=?, Stock=? WHERE SKU=?", (name, price, stock, sku))
    conn.commit()
    conn.close()
