import sqlite3
import sys
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
sock.connect(server_address)


def create_product(Nombre, Precio, Stock, SKU, Categoria):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("INSERT INTO inventario (Nombre, Precio, Stock, SKU, Categoria) VALUES (?, ?, ?, ?, ?)", (Nombre, Precio, Stock, SKU, Categoria))
    conn.commit()
    conn.close()

try:
    # Send data
    message = b"00080sinitserv1"
    print ('sending {!r}'.format (message))
    sock.sendall(message)
    while True:
        # Look for the response
        print ("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv (5))
        while amount_received < amount_expected:
            data = sock.recv(amount_received - amount_expected)
            amount_received+=len(data)
            Nombre = data[0]
            Precio = data[1]
            Stock = data[2]
            SKU = data[3]
            Categoria= data[4]
            create_product(Nombre, Precio, Stock, SKU, Categoria)
            print ('received {!r}'.format (data))

finally:
    print ('closing socket')
    sock.close()
