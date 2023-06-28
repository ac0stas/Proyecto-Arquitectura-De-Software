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
    message = b"00080sinitserv1"
    print('sending {!r}'.format(message))
    sock.sendall(message)

    while True:
        print("Waiting for transaction")
        data_length = sock.recv(5)
        if data_length:
            amount_expected = int(data_length)
            data = b''
            while len(data) < amount_expected:
                packet = sock.recv(amount_expected - len(data))
                if not packet:
                    break
                data += packet
            if len(data) == amount_expected:  # Confirm that we received the expected amount of data
                try:
                    Nombre, Precio, Stock, SKU, Categoria = data
                    create_product(Nombre, Precio, Stock, SKU, Categoria)
                    print('received {!r}'.format(data))
                except ValueError:
                    print("Error: Received more data than expected")
            else:
                print('Unexpected data format or length received')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print('closing socket and database connection')
    sock.close()




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



