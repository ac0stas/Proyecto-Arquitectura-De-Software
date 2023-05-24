import sqlite3

def delete_product(sku):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute("DELETE FROM Productos WHERE SKU=?", (sku,))
    conn.commit()
    conn.close()
