import sqlite3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)

sock.connect(server_address)

message = b"00050sinitserv3"

def delete_product(sku):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute("DELETE FROM Productos WHERE SKU=?", (sku,))
    conn.commit()
    conn.close()
