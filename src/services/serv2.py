import sqlite3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)

sock.connect(server_address)

message = b"00050sinitserv2"

def buscar_producto(sku):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT FROM inventario WHERE SKU=?", (sku,))
    conn.commit()
    conn.close()
    return c.fetchall()
